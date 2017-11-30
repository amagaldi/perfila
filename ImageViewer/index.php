<html>
  <?php
    include("queries.php");
  ?>
  <head>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
    <link rel="stylesheet" href="css/main.css">
  </head>
  
  <body>
  
	<div class="container-fluid red ">
		<div class="row">
			<!--<div class="loader" id="loader" style="display: block;"></div>-->
			<div class="col-lg-6 col-md-6 col-sm-6  col-xs-12 ">
				<canvas id="ppi_canvas" width="100%" ></canvas>
				<?php 
					$jsObj = 'ppiAnim';//This name MUST be harcoded
					include 'animControls.php';
				?>
			</div>        
			<div class="col-lg-6 col-md-6 col-sm-6  col-xs-12" >
				<canvas id="rhi_canvas" width="100%"></canvas>
				<?php 
					$jsObj = 'rhiAnim';//This name MUST be harcoded
					include 'animControls.php';
				?>
			</div>
		</div>
		<div class="row">
			<div class="col-lg-6 col-md-6 col-sm-6  col-xs-12" >
				<canvas id="all_winds_canvas" width="100%"></canvas>
				<?php 
					$jsObj = 'all_winds_anim';//This name MUST be harcoded
					include 'animControls.php';
				?>
			</div>
			<div class="col-lg-6 col-md-6 col-sm-6  col-xs-12" >
				<canvas id="wind_mag_canvas" width="100%"></canvas>
				<?php 
					$jsObj = 'wind_mag_anim';//This name MUST be harcoded
					include 'animControls.php';
				?>
			</div>
		</div>

    <footer class="footer">
      <div class="d-flex justify-content-end" style="height: 65px;">

      <p class="mr-auto p-2">By <a href='https://www.atmosfera.unam.mx/ciencias-atmosfericas/modelos-climaticos/alejandro-aguilar-sierra'>M. S. Alejandro Aguilar</a>, <a href='http://olmozavala.com'>Ph.D. Olmo Zavala</a> and <a href="https://github.com/ixchelzg">M.S. Ixchel Zazueta</a>, 2017</p>
          <img src="img/goes-r-page-logo.png" class="nav_logo_min" />
          <img src="img/IG.png" class="nav_logo_min"  />
          <img src="img/unam.png" class="nav_logo_min"  />
          <img src="img/logo.png" class="nav_logo_min"  />
      </div>

    </footer>

  </div>

    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>

    <script > var img_names= <?php echo json_encode($img_names); ?>;</script>
    <script > 
//		console.log(img_names);
//		console.log(last_image);
	</script>
    <script src="js/Tools.js"></script>
    <script src="js/Animation.js"></script>
    <script src="js/animations.js"></script>
  </body>
</html>