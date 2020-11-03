<?php
    session_start();
    $target_dir = './';
    $file = '/var/www/html/files.zip';
    if(!file_exists($file)) die("I'm sorry, the file doesn't seem to exist.");
    
    header('Content-Description: File Transfer');
    header('Content-Type: application/octet-stream');
    
    header('Content-Disposition: attachment;filename="'.basename($file).'"');
    header('Content-Transfer-Encoding: binary'); 
    header('Pragma: public'); 
    header('Content-Length: ' . filesize($file));
    readfile($file);
    exit;
?>

