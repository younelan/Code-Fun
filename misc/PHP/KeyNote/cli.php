<?php
require_once 'ParseKNT.php';

$cliOptions = getopt("f:"); // e.g. -f /path/to/file.knt
$filename = isset($cliOptions['f']) ? $cliOptions['f'] : (__DIR__ . '/notes.knt');

$parser = new ParseKNT();
$parser->parse($filename);

function printNotes($notes, $indent = 0) {
    foreach ($notes as $note) {
        $title = isset($note['properties']['ND']) ? $note['properties']['ND'] : 'No Title';
        echo str_repeat("  ", $indent) . $title . PHP_EOL;
        if (!empty($note['rtf'])) {
            echo str_repeat("  ", $indent + 1) . rtfToHtml($note['rtf']) . PHP_EOL;
        }
        if (isset($note['children']) && is_array($note['children'])) {
            printNotes($note['children'], $indent + 1);
        }
    }
}

foreach ($parser->sections as $section) {
    $sectionTitle = isset($section['properties']['NN']) ? $section['properties']['NN'] : 'No Section Title';
    echo "Section: " . $sectionTitle . PHP_EOL;
    if (!empty($section['notes'])) {
        printNotes($section['notes']);
    }
}
?>
