<?php
require_once 'ParseKNT.php';

// Hard-coded list of available files.
$files = [
    'notes.knt'   => 'notes.knt',
];

// Determine selected file from GET, defaulting to sample.knt.
$selectedFileKey = isset($_GET['file']) && array_key_exists($_GET['file'], $files) ? $_GET['file'] : 'sample.knt';
$selectedFile = $files[$selectedFileKey];

$parser = new ParseKNT();
$parser->parse($selectedFile);
$notesTree = $parser->sections;
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Keynote Viewer</title>
    <style>
        body { font-family: Arial, sans-serif; margin:0; }
        #tabs { background:#ddd; padding:10px; }
        #tabs a { color: #000; padding: 8px 12px; margin-right:5px; text-decoration: none; background:#eee; border:1px solid #ccc; }
        #tabs a.active { background:#fff; border-bottom: none; }
        #container { display: flex; height: calc(100vh - 50px); }
        #tree { 
            width: 250px; 
            min-width: 250px;  /* ensures tree remains visible */
            border-right: 1px solid #ccc; 
            overflow-y: auto; 
            padding:10px; 
            resize: horizontal;  /* allow horizontal resizing */
        }
        #content { padding:20px; flex-grow: 1; overflow-y: auto; }
        .tree-node { cursor:pointer; margin-bottom:5px; }
        .child { margin-left: 15px; }
    </style>
    <script>
        function showNote(contentId) {
            var noteDiv = document.getElementById(contentId);
            var contentDiv = document.getElementById("content");
            contentDiv.innerHTML = noteDiv.innerHTML; // set note content into the content area
        }
        function showSections() {
            var contentDiv = document.getElementById("content");
            var sectionsDiv = document.getElementById("sectionsContent");
            contentDiv.innerHTML = sectionsDiv.innerHTML;
        }
    </script>
</head>
<body>
<div id="tabs">
    <?php foreach($files as $key => $path): ?>
        <a href="?file=<?php echo urlencode($key); ?>" <?php echo ($key==$selectedFileKey) ? 'class="active"' : ''; ?>>
            <?php echo htmlspecialchars($key); ?>
        </a>
    <?php endforeach; ?>
    <a href="javascript:showSections();">Sections</a> <!-- New tab for Sections -->
</div>
<div id="container">
    <div id="tree">
        <?php 
        // Recursive function to build the tree.
        function renderTree($notes, $prefix = 'note') {
            static $counter = 0;
            foreach($notes as $note) {
                $counter++;
                $nodeId = $prefix . $counter;
                // Convert note title using iconv for proper accents.
                $title = isset($note['properties']['ND']) ? $note['properties']['ND'] : 'No Title';
                $title = iconv("WINDOWS-1252", "UTF-8//TRANSLIT", $title);
                echo '<div class="tree-node" onclick="showNote(\''.$nodeId.'\')">'.htmlspecialchars($title).'</div>';
                if(isset($note['children']) && is_array($note['children'])){
                    echo '<div class="child">';
                    renderTree($note['children'], $prefix);
                    echo '</div>';
                }
                // Store note content in a hidden div.
                echo '<div id="'.$nodeId.'" class="noteContent" style="display:none;">';
                echo (isset($note['rtf']) && $note['rtf']) ? rtfToHtml($note['rtf']) : '<em>No content</em>';
                echo '</div>';
            }
        }
        foreach($notesTree as $section){
            if(!empty($section['notes'])){
                renderTree($section['notes']);
            }
        }
        ?>
    </div>
    <div id="content">
        <h2>Note Content</h2>
        <p>Click a note on the left to display its content here.</p>
    </div>
</div>
<!-- Hidden container for sections with detailed properties -->
<div id="sectionsContent" style="display:none;">
    <h2>Sections</h2>
    <?php foreach($notesTree as $section): ?>
        <div class="section" style="margin-bottom:15px;">
            <?php
            // Use section title from ND if available; otherwise, use "Section"
            $sectionTitle = isset($section['properties']['ND']) ? $section['properties']['ND'] : "Section";
            $sectionTitle = iconv("WINDOWS-1252", "UTF-8//TRANSLIT", $sectionTitle);
            ?>
            <strong><?php echo htmlspecialchars($sectionTitle); ?></strong>
            <?php foreach($section['properties'] as $key => $value): 
                // Skip ND as it's already used for title
                if ($key == 'ND') continue;
                $propKey = iconv("WINDOWS-1252", "UTF-8//TRANSLIT", $key);
                $propValue = iconv("WINDOWS-1252", "UTF-8//TRANSLIT", $value);
            ?>
                <p><?php echo htmlspecialchars($propKey.': '.$propValue); ?></p>
            <?php endforeach; ?>
        </div>
    <?php endforeach; ?>
</div>
</body>
</html>
