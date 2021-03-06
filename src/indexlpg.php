<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <title>FEPrepare</title>
      <!-- Bootstrap core CSS -->
      <link href="css/bootstrap.min.css" rel="stylesheet">
   </head>
   <body style="text-align: center;">
      <!-- Main jumbotron for a primary marketing message or call to action -->
      <div class="jumbotron" style="background-color: AntiqueWhite ;">
         <div class="container-fluid">
            <h1 class="display-3"><a href='index.php'>FEPrepare </a></h1>
            <p>This is a set-up tool for NAMD/FEP. This tool automates the set-up procedure for NAMD. It uses VMD to aquire the FEP files needed for the simulation. It will provide you with all the files you need to run a simulation in NAMD. Just follow the steps. For more information please read the manual</p>

          </div>
      </div>
       <div class="row">
		<div class="row1">
	
		<div>
	       <p style="float:left; width:100px;height:50px; margin-left: 3rem; "><input class="btn btn-primary" type="button" name ="LigParGen" value="LigParGen Files" onclick="location.href='indexlpg.php'" /> </p>
          </div>
	     <div>
	       <p style="float:right; width:100px;height:50px; margin-right: 5rem; "><input class="btn btn-primary" type="button" name ="CGenFF" value="CGenFF Files" onclick="location.href='indexcgf.php'" /> </p>
             </div>
		 </div>
             <div class="btn-group btn-group-justified">
              <div class="btn-group">
               <p style="float:left; margin-right: 1rem;"><input class="btn btn-info" type="button" name = "Manual" value="Manual"  onClick="window.open('Manual.pdf')"/></p>
              </div>
              <div class="btn-group">
               <p style="float:left; margin-right: 1rem;"><input class="btn btn-info" type="button" name = "video" value="Video example" onClick="window.open('VideoExample.mp4')"/></p>
              </div>
              <div class="btn-group">
               <p style="float:right; "><input class="btn btn-info" type="button" name = "example" value="Download example" onclick="location.href='downloadexample.php'"/></p>
              </div>
             </div>
         </div>
     <div class="container-fluid">
         <div class="row">
		<h4>Upload all requested files in order to proceed:<br></br></h4>			
            <form action="upload.php" method="post" enctype="multipart/form-data">
             <div class="col-sm">
                    Select the reference .pdb file<input name="fileToUpload[]" id="fileToUpload" type="file" accept=".pdb" multiple> Select the mutant .pdb file<input name="fileToUpload[]" id="fileToUpload" type="file" accept=".pdb" multiple>
             </div>
             <div class="col-sm">
                    Select the reference &nbsp;.rtf &nbsp;file<input name="fileToUpload[]" id="fileToUpload" type="file" accept=".rtf" multiple> Select the mutant &nbsp;.rtf &nbsp;file<input name="fileToUpload[]" id="fileToUpload" type="file" accept=".rtf" multiple>
             </div>
             <div class="col-sm">
                  Select the reference .prm file<input name="fileToUpload[]" id="fileToUpload" type="file" accept=".prm" multiple> Select the mutant .prm file<input name="fileToUpload[]" id="fileToUpload" type="file" accept=".prm" multiple>
             </div>
                  <br>
                  <p align="center"> Select the protein .pdb file<input name="fileToUpload[]" id="fileToUpload" type="file" accept=".pdb" multiple> </p>
                  <input type="submit" value="Upload" class="btn btn-primary btn-lg"/></p>

           </form>
         </div>
      </div>


         <br>
	
	 <br>
         <hr>
         <img src="logo-brfaa.jpg" style="width:100px;height:50px;" alt="logo1"/>
         <img src="Grnet-transp.jpg" style="width:100px;height:50px;" alt="logo2"/>
         <img src="images/logo_VISEEM_FINAL_WEB.jpg" style="width:100px;height:50px;" alt="logo3"/>
         <img src="eu__flag_of_europe.png" style="width:100px;height:50px;" alt="logo4"/><br>
         VI-SEEM receives funding from the European Union’s Horizon 2020 research<br>
         and innovation programme under grant agreement No 675121<br><br><br>
         Created by Stamatia Zavitsanou & Georgios Galanopoulos<br>
         Powered by Cournia lab<br>
         Contact support: zavitsanoustamatia@gmail.com
      </footer>
      <br/>
      <br/>
   </body>
</html>
