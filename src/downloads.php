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
            <h1 class="display-3">A set-up tool for NAMD/FEP</h1>
            <p>This tool automates the set-up procedure for NAMD. It uses VMD to aquire the FEP files needed for the simulation. It will provide you with all the files you need to run a simulation in NAMD. Just follow the steps. For more information please read the manual</p>

         </div>
      </div>
      <div class="container-fluid">
         <div class="row">
                  <input type="submit" name = "zip" value="Download files" onclick="location.href='download.php'" class="btn btn-primary btn-lg">
               </p>
            </div>
            <p><input type="submit" name = "return" onclick="location.href='index.php'" value="Return"/></p>
            <br/>
            <br/>
            <br/>
            <div id="dom-target" style="display: none;">
               <?php 
                  session_start();
                  $name = 'downloads';
                  echo htmlspecialchars($name); /* You have to escape the result will not be valid HTML otherwise. */
                  ?>
            
         </div>
      </div>
      <br/>
      <br/>
      <br/>
      <hr>
      <footer>
         <div class="row">
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

