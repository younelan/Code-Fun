<?php
class ParseKNT {
    public $sections = [];
    
    public function parse($filepath) {
        $lines = file($filepath, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
        if (!$lines) {
            throw new Exception("Unable to read file: $filepath");
        }
        // Verify file signature
        foreach ($lines as $line) {
            $trim = trim($line);
            if ($trim === '') continue;
            if (strpos($trim, '#!GFKNT') === 0) break;
            else throw new Exception("Invalid file signature");
        }
        
        $currentSection = null;
        $noteStack = [];
        $currentNote = null;
        $mode = null;
        
        foreach ($lines as $line) {
            $line = rtrim($line, "\r\n");
            
            // If in note_rtf mode, check for control code markers to end the block.
            if ($mode === 'note_rtf') {
                if (preg_match('/^(%:|%\+|%-|%%)/', $line)) {
                    // Finalize the current note's rtf block
                    $lv = isset($currentNote['properties']['LV']) ? (int)$currentNote['properties']['LV'] : 0;
                    while (!empty($noteStack) && end($noteStack)['level'] >= $lv) {
                        array_pop($noteStack);
                    }
                    $currentNote['level'] = $lv;
                    if (empty($noteStack)) {
                        $currentSection['notes'][] = $currentNote;
                        $noteStack[] = &$currentSection['notes'][count($currentSection['notes']) - 1];
                    } else {
                        $parent = & $noteStack[count($noteStack) - 1];
                        $parent['children'][] = $currentNote;
                        $noteStack[] = & $parent['children'][count($parent['children']) - 1];
                    }
                    $currentNote = null;
                    $mode = null;
                    // Now process the current line as a new control code.
                } else {
                    $currentNote['rtf'] .= $line . "\n";
                    continue;
                }
            }
            
            if (strpos($line, '%+') === 0) {
                if ($currentSection) {
                    $this->sections[] = $currentSection;
                }
                $currentSection = ['properties' => [], 'notes' => []];
                $noteStack = [];
                $mode = 'section';
                continue;
            }
            if (strpos($line, '%-') === 0) {
                // If a new note delimiter is encountered while in note mode, finalize any active note.
                if ($mode === 'note_rtf' && $currentNote !== null) {
                    // (This case should be normally handled above)
                }
                $currentNote = ['properties' => [], 'children' => []];
                $mode = 'note';
                continue;
            }
            if (strpos($line, '%:') === 0) {
                $mode = 'note_rtf';
                $currentNote['rtf'] = '';
                continue;
            }
            if (strpos($line, '%%') === 0) {
                continue;
            }
            
            // Process based on mode.
            if ($mode === 'section') {
                if (strpos($line, '=') !== false) {
                    list($key, $value) = explode('=', $line, 2);
                    $currentSection['properties'][trim($key)] = trim($value);
                }
            } elseif ($mode === 'note') {
                if (strpos($line, '=') !== false) {
                    list($key, $value) = explode('=', $line, 2);
                    $currentNote['properties'][trim($key)] = trim($value);
                }
            }
        }
        // Finalize an unfinished rtf note if file ended in that mode.
        if ($mode === 'note_rtf' && $currentNote !== null) {
            $lv = isset($currentNote['properties']['LV']) ? (int)$currentNote['properties']['LV'] : 0;
            while (!empty($noteStack) && end($noteStack)['level'] >= $lv) {
                array_pop($noteStack);
            }
            $currentNote['level'] = $lv;
            if (empty($noteStack)) {
                $currentSection['notes'][] = $currentNote;
            } else {
                $parent = end($noteStack);
                $parent['children'][] = $currentNote;
            }
        }
        if ($currentSection) {
            $this->sections[] = $currentSection;
        }
    }
}

// Helper function for RTF to HTML conversion.
function rtfToHtml($rtf, $convertEntities = true) {
    $html = $rtf;
    // Remove font table entirely (using recursive regex)
    $html = preg_replace('/\{\\\\fonttbl(?:(?>[^{}]+)|(?R))*\}/s', '', $html);
    // Remove deflang commands (e.g. "\deflang1045")
    $html = preg_replace('/\\\\deflang\d+\b/', '', $html);
    // Remove generator comments
    $html = preg_replace('/\{\\\\\*\\\\generator [^}]+\}/s', '', $html);
    // Extract and remove the color table
    if (preg_match('/\{\\\\colortbl(.*?)\}/s', $html, $cMatch)) {
        $html = str_replace($cMatch[0], '', $html);
    }
    // Remove any leftover color codes (\cfN)
    $html = preg_replace('/\\\\cf\d+\b\s*/', '', $html);
    // Convert hyperlinks
    $html = preg_replace_callback('/\{\\\\field\{\\\\\*\\\\fldinst\{HYPERLINK "([^"]+)"\}\}\{\\\\fldrslt\{([^}]+)\}\}\}/', function($m) {
        return '<a href="'.$m[1].'">'.$m[2].'</a>';
    }, $html);
    // Replace paragraph markers with <br>
    $html = preg_replace('/\\\\par/', '<br>', $html);
    // Bold: \b -> <strong>, \b0 -> </strong>
    $html = preg_replace('/\\\\b0\b/', '</strong>', $html);
    $html = preg_replace('/\\\\b\b/', '<strong>', $html);
    // Italic and underline conversions
    $html = preg_replace('/\\\\i0\b/', '</em>', $html);
    $html = preg_replace('/\\\\i\b/', '<em>', $html);
    $html = preg_replace('/\\\\ulnone\b/', '</u>', $html);
    $html = preg_replace('/\\\\ul\b/', '<u>', $html);
    // Replace RTF accent escapes (e.g. \'a9) with their actual characters
    $html = preg_replace_callback("/\\\\'([0-9A-Fa-f]{2})/", function($m) {
        return chr(hexdec($m[1]));
    }, $html);
    // Remove remaining RTF control words and braces
    $html = preg_replace('/\\\\[a-zA-Z]+\d*\b\s*/', '', $html);
    $html = str_replace(['{','}'], '', $html);
    if ($convertEntities) {
        // Determine the code page from the RTF using the \ansicpg control word.
        $codePage = "WINDOWS-1252"; // default if not found
        if (preg_match('/\\\\ansicpg(\d+)/', $rtf, $matches)) {
            $codePage = "WINDOWS-" . $matches[1]; // e.g. WINDOWS-1250 for \ansicpg1250
        }
        $html = iconv($codePage, "UTF-8//TRANSLIT", $html); // conversion using detected code page
    }
    return $html;
}
?>
