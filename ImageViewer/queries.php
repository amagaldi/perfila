<?php
	session_start();

	$currDate = date("Y-m-d"); #initializes with today's day
//	$currDate = "2017-11-30"; #initializes with today's day
	$currFolder = "images/" . $currDate . "/";

	$ruta_completa = $currFolder ."/". $ImageNom;

	$img_names = glob($currFolder. "*.png");
?>