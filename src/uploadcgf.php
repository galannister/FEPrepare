<?php
session_start(); 
$target_dir ='/var/www/html/Feprepare/media/downloads/';
foreach ($_FILES["fileToUpload"]["name"] as $f => $name) {
 $target_file = $target_dir.basename($_FILES["fileToUpload"]["name"][$f]);
 $uploadOk = 1;
 $fileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
 $fileName = pathinfo($target_file,PATHINFO_FILENAME)."_".date('mdYHis');
 $fileName2 = pathinfo($target_file,PATHINFO_FILENAME);
 $_SESSION["filenm"][$f] = $fileName2;
 $countfiles = count($_FILES["fileToUpload"]["name"]);
// Check file size
 //if ($_FILES["fileToUpload"]["size"] > 500000) {
   // echo "Sorry, your file is too large.";
    //$uploadOk = 0;
 //}
// Check if $uploadOk is set to 0 by an error 
 if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
 } else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"][$f], $target_dir.$fileName.".".$fileType)){
        #echo " The file has been uploaded. ";
        $ela[$f]= $fileName.".".$fileType;//+$ch;
        $ela2[$f]=$fileName2.".".$fileType;
        #echo ($ela[$f]);
        

   
 } else {
        echo "Sorry, there was an error uploading your file.";
    }
 }
}
shell_exec("cd /var/www/html/Feprepare/media/downloads");
system("cp /var/www/html/Feprepare/media/downloads/$ela[0] /var/www/html/Feprepare/media/downloads/reference.pdb");
shell_exec("python rtfhandlerref.py /var/www/html/Feprepare/media/downloads/$ela[2] /var/www/html/Feprepare/media/downloads/$ela[0]");
shell_exec("python rtfhandlermut.py /var/www/html/Feprepare/media/downloads/$ela[3] /var/www/html/Feprepare/media/downloads/$ela[1]");
shell_exec("python sort.py ");
shell_exec("python dualTop.py ");
shell_exec("python hybridpdb.py /var/www/html/Feprepare/media/downloads/$ela[0] /var/www/html/Feprepare/media/downloads/$ela[1]");
shell_exec("python complex1.py /var/www/html/Feprepare/media/downloads/$ela[4]");
shell_exec("python split_chainsC.py /var/www/html/Feprepare/media/downloads/$ela[4] /var/www/html/ligand.pdb");
shell_exec("python strhandler.py /var/www/html/Feprepare/media/downloads/$ela[2] /var/www/html/Feprepare/media/downloads/reference.prm");
shell_exec("python strhandler.py /var/www/html/Feprepare/media/downloads/$ela[3] /var/www/html/Feprepare/media/downloads/mutant.prm");
system("cp /var/www/html/Feprepare/media/downloads/final.txt /var/www/html/Feprepare/media/downloads/solvent/ligand.rtf");
system("cp /var/www/html/Feprepare/media/downloads/final.txt /var/www/html/Feprepare/media/downloads/complex/ligand.rtf");
system("cp /var/www/html/mutant.rtf /var/www/html/Feprepare/media/downloads/mutant.rtf");


system("cp /var/www/html/complex.pdb /var/www/html/Feprepare/media/downloads/complex/complex.pdb");
system("cp /var/www/html/complex.pdb /var/www/html/Feprepare/media/downloads/solvent/complex.pdb");
system("cp /var/www/html/Feprepare/media/downloads/psfgen /var/www/html/Feprepare/media/downloads/complex/psfgen");
system("cp /var/www/html/Feprepare/media/downloads/psfgen /var/www/html/Feprepare/media/downloads/solvent/psfgen");




system("cp vmd_prepare_complex_after_gui_autopsf /var/www/html/Feprepare/media/downloads/complex/vmd_prepare_complex_after_gui_autopsf");
system("cp vmd_prepare_ligand_after_gui_autopsf /var/www/html/Feprepare/media/downloads/solvent/vmd_prepare_ligand_after_gui_autopsf");




#system("chmod 777 /var/www/html/Feprepare/media/downloads/reference.pdb ");
#system("chmod 777 /var/www/html/mutant.rtf");
system("cp /var/www/html/hybrid.pdb /var/www/html/Feprepare/media/downloads/solvent/hybrid.pdb");

system("cp /var/www/html/hybrid.pdb /var/www/html/Feprepare/media/downloads/complex/hybrid.pdb");



#system("chmod 777 /var/www/html/Feprepare/media/downloads/solvent/reference.pdb ");
#system("chmod 777 /var/www/html/Feprepare/media/downloads/solvent/mutant.rtf");

$id = 2;
echo "<script>location.href='downloads.php?id=$id&msg=succesfully redirect';</script>";
chdir ('/var/www/html/Feprepare/media/downloads/complex');
system("vmd -dispdev text -e psfgen");
#system("chmod 777 psf-complex.pdb");
#system("chmod 777 psf-complex.psf");
system("vmd -dispdev text -e vmd_prepare_complex_after_gui_autopsf > vmd_log.txt");
#system("chmod 777 vmd_log.txt");
#system("chmod 777 ionized.pdb");
system('cp ionized.pdb ionized.fep');
#system('chmod 777 ionized.fep');
chdir ('/var/www/html/Feprepare/media/downloads/solvent');
system("vmd -dispdev text -e psfgen_solv");
#system("chmod 777 psf-solvated.pdb");
#system("chmod 777 psf-solvated.psf");
system("vmd -dispdev text -e vmd_prepare_ligand_after_gui_autopsf > vmd_log.txt");
#system("chmod 777 vmd_log.txt");
system("chmod 777 ionized.pdb");
system('cp ionized.pdb ionized.fep');
#system('chmod 777 ionized.fep');

chdir ('/var/www/html/');
#system("cp /opt/lampp/htdocs/Feprepare/media/downloads/$ela[0] .");
shell_exec("python fep1.py /var/www/html/Feprepare/media/downloads/complex/ionized.fep /var/www/html/Feprepare/media/downloads/solvent/ionized.fep /var/www/html/Feprepare/media/downloads/complex/ionized.pdb /var/www/html/Feprepare/media/downloads/solvent/ionized.pdb");

shell_exec("python min-max.py /var/www/html/Feprepare/media/downloads/complex/vmd_log.txt /var/www/html/Feprepare/media/downloads/solvent/vmd_log.txt");

// Get real path for our folder
$rootPath = realpath('/var/www/html/Feprepare/media/downloads');

// Initialize archive object
$zip = new ZipArchive();
$zip->open('files.zip', ZipArchive::CREATE | ZipArchive::OVERWRITE);

// Create recursive directory iterator
/** @var SplFileInfo[] $files */
$files = new RecursiveIteratorIterator(
    new RecursiveDirectoryIterator($rootPath),
    RecursiveIteratorIterator::LEAVES_ONLY
);

foreach ($files as $name => $file)
{
    // Skip directories (they would be added automatically)
    if (!$file->isDir())
    {
        // Get real and relative path for current file
        $filePath = $file->getRealPath();
        $relativePath = substr($filePath, strlen($rootPath) + 1);

        // Add current file to archive
        $zip->addFile($filePath, $relativePath);
    }
}
$zip->close();
system("cp /var/www/html/Feprepare/media/downloads/files.zip /var/www/html/files.zip");

#header("Location: downloads.php");
?>
