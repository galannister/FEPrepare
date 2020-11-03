<?php
session_start(); 
$target_dir ='./FEPrepare/media/documents/';
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
        
        $ela[$f]= $fileName.".".$fileType;//+$ch;
        $ela2[$f]=$fileName2.".".$fileType;
        echo ($ela[$f]);
        

        #system("rm -rf $target_dir/*");
        #system("rm -rf $target_dir/../*.txt");
        #system('find media/downloads/ -mmin +1440 -type f -name "*.prm" -exec rm -rf {} \;');
        #system('find media/downloads/ -mmin +1440 -type f -name "*.pdb" -exec rm -rf {} \;');
        #system('find media/downloads/ -mmin +1440 -type f -name "*.rtf" -exec rm -rf {} \;');
        #if ($outpt == done){
            #header('Location: downloads.php');
        #}
        #else {
        #echo "Sorry, wrong input. Please read the manual or else contact us.";
         # }
   
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
 }
}

shell_exec("python names3.py ./FEPrepare/media/documents/$ela[0] ./FEPrepare/media/documents/$ela[1] ./FEPrepare/media/documents/$ela[2] ./FEPrepare/media/documents/$ela[3] ./FEPrepare/media/documents/$ela[4] ./FEPrepare/media/documents/$ela[5]");
shell_exec("python merge2.py newligandArtf.txt newligandBrtf.txt > sortedB");
shell_exec("python dual2.py");
shell_exec("python complex.py ./FEPrepare/media/documents/$ela[6]");
shell_exec("python split_chains.py complex newligandA.txt");

system("cp updatedprm.txt ./FEPrepare/media/downloads/updated.prm" );

$currentFilePath = 'complex';   
$newFilePath = './FEPrepare/media/downloads/complex.pdb';
$fileMoved = copy($currentFilePath, $newFilePath);

$currentFilePath = 'newligandA.txt';
$newFilePath = "./FEPrepare/media/downloads/$ela2[0]";
$fileMoved = copy($currentFilePath, $newFilePath);

$currentFilePath = 'newligandB.txt';
$newFilePath = "./FEPrepare/media/downloads/$ela2[1]";
$fileMoved = copy($currentFilePath, $newFilePath);

$currentFilePath = 'newligandArtf.txt';
$newFilePath = "./FEPrepare/media/downloads/$ela2[2]";
$fileMoved = copy($currentFilePath, $newFilePath);

$currentFilePath = 'newligandBrtf.txt';
$newFilePath = "./FEPrepare/media/downloads/$ela2[3]";
$fileMoved = copy($currentFilePath, $newFilePath);

$currentFilePath = 'newligandAprm.txt';
$newFilePath = "media/downloads/$ela2[4]";
$fileMoved = copy($currentFilePath, $newFilePath);

$currentFilePath = 'newligandBprm.txt';
$newFilePath = "media/downloads/$ela2[5]";
$fileMoved = copy($currentFilePath, $newFilePath);

$currentFilePath = 'hybridpdb.txt';
$newFilePath = './FEPrepare/media/downloads/ligand.pdb';
$fileMoved = copy($currentFilePath, $newFilePath);

$currentFilePath = 'final.txt';
$newFilePath = './FEPrepare/media/downloads/ligand.rtf';
$fileMoved = copy($currentFilePath, $newFilePath);

$currentFilePath = 'top_opls_aam.inp';
$newFilePath = './FEPrepare/media/downloads/top_opls_aam.inp';
$fileMoved = copy($currentFilePath, $newFilePath);

$currentFilePath = 'par_opls_aam.inp';
$newFilePath = 'media/downloads/par_opls_aam.inp';
$fileMoved = copy($currentFilePath, $newFilePath);

$currentFilePath = 'fep.tcl';
$newFilePath = './FEPrepare/media/downloads/fep.tcl';
$fileMoved = copy($currentFilePath, $newFilePath);

system("cp vmd_prepare_complex_after_gui_autopsf ./FEPrepare/media/downloads/complex/vmd_prepare_complex_after_gui_autopsf");
system("cp vmd_prepare_ligand_after_gui_autopsf ./FEPrepare/media/downloads/solvent/vmd_prepare_ligand_after_gui_autopsf");

system("chmod 777 psfgen ");
system("cp psfgen ./FEPrepare/media/downloads/complex/psfgen");

system("chmod 777 ./FEPrepare/media/downloads/ligand.pdb ");
system("chmod 777 ./FEPrepare/media/downloads/ligand.rtf");
system("cp ./FEPrepare/media/downloads/ligand.pdb media/downloads/solvent/ligand.pdb");
system("cp ./FEPrepare/media/downloads/ligand.rtf media/downloads/solvent/ligand.rtf");
system("cp ./FEPrepare/media/downloads/top_opls_aam.inp media/downloads/solvent/top_opls_aam.inp");

system("chmod 777 ./FEPrepare/media/downloads/solvent/ligand.pdb ");
system("chmod 777 ./FEPrepare/media/downloads/solvent/ligand.rtf");
system("chmod 777 ./FEPrepare/media/downloads/solvent/top_opls_aam.inp");

system('cp ./FEPrepare/media/downloads/complex/psfgen media/downloads/solvent/psfgen');
system('cp psfgen_solv ./FEPrepare/media/downloads/solvent/psfgen_solv');

system("chmod 777 ./FEPrepare/media/downloads/complex/psfgen media/downloads/solvent/psfgen ");
system("chmod 777 ./FEPrepare/media/downloads/solvent/psfgen_solv");

chdir ('./FEPrepare/media/downloads/complex');
shell_exec("./run_vmd_tmp -dispdev text -e psfgen");
system("chmod 777 psf-complex.pdb");
system("chmod 777 psf-complex.psf");
shell_exec("./run_vmd_tmp -dispdev text -e vmd_prepare_complex_after_gui_autopsf > vmd_log.txt");
system("chmod 777 vmd_log.txt");
system("chmod 777 ionized.pdb");
system('cp ionized.pdb ionized.fep');
system('chmod 777 ionized.fep');

chdir ('/var/www/html/FEPrepare/media/downloads/solvent');
shell_exec("./run_vmd_tmp -dispdev text -e psfgen_solv");
system("chmod 777 psf-solvated.pdb");
system("chmod 777 psf-solvated.psf");
shell_exec("./run_vmd_tmp -dispdev text -e vmd_prepare_ligand_after_gui_autopsf > vmd_log.txt");
system("chmod 777 vmd_log.txt");
system("chmod 777 ionized.pdb");
system('cp ionized.pdb ionized.fep');
system('chmod 777 ionized.fep');

chdir ('/var/www/html/FEPrepare/');
system("cp media/downloads/ligand.pdb .");
shell_exec("python fep.py ./FEPrepare/media/downloads/complex/ionized.fep ./FEPrepare/media/downloads/solvent/ionized.fep ./FEPrepare/media/downloads/complex/ionized.pdb ./FEPrepare/media/downloads/solvent/ionized.pdb");

shell_exec("python min-max.py ./FEPrepare/media/downloads/complex/vmd_log.txt ./FEPrepare/media/downloads/solvent/vmd_log.txt");
// Get real path for our folder
$rootPath = realpath('./FEPrepare/media/downloads');

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
header('Location: downloads.php');
system('find ./FEPrepare/media/downloads/ -mmin +1440 -type f -name "*.prm" -exec rm -rf {} \;');
system('find ./FEPrepare/media/downloads/ -mmin +1440 -type f -name "*.pdb" -exec rm -rf {} \;');
system('find ./FEPrepare/media/downloads/ -mmin +1440 -type f -name "*.rtf" -exec rm -rf {} \;');
?>
