/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

var ppiAnim;
var rhiAnim;
var all_winds_anim;
var wind_mag_anim;

$( window ).resize(function() {
	ppiAnim.updateSize();
	rhiAnim.updateSize();
	all_winds_anim.updateSize();
	wind_mag_anim.updateSize();
});



$(function () {
	$('[data-toggle="tooltip"]').tooltip({
		trigger : 'hover'
	});
	$('.popover-dismiss').popover({
		trigger: 'hover'
	});

	// This object contains the names of the PPI images
	var ppiNames = filterNames(img_names, 'PPI');
				
	ppiAnim = new Animation(ppiNames, 'ppi_canvas', 'ppiAnim');
	//Start loading the images and playing the animation. 
	// It starts with a height of 50% of the window size
	ppiAnim.init();

	// This object contains the names of the RHI images
	var rhiNames = filterNames(img_names, 'RHI');
	rhiAnim = new Animation(rhiNames, 'rhi_canvas', 'rhiAnim');
	rhiAnim.init();

	var all_winds_Names = filterNames(img_names, 'Allvel');
	all_winds_anim = new Animation(all_winds_Names, 'all_winds_canvas', 'all_winds_anim');
	all_winds_anim.init();

	var wind_mag_Names = filterNames(img_names, 'Magnitude');
	wind_mag_anim = new Animation(wind_mag_Names, 'wind_mag_canvas', 'wind_mag_anim');
	wind_mag_anim.init();

});

function toggledisplay(elementID)
{
	(function(style) {
		style.display = style.display === 'none' ? '' : 'none';
	})(document.getElementById(elementID).style);
}

image_type = "jpg";                   //"gif" or "jpg" or whatever your browser can display

first_image_name = 0;     //Representa el nombre de la primer imagen
first_image = 0;                      //first image number
speed_text = 0;
var inicioPlayfwd = false;    //Controla la animacion si esta en play o en stop
var inicioPlayBkw = false;    //Controla la animacion cuando esta en reversa

//=== THE CODE STARTS HERE - no need to change anything below ===
//=== global variables ====
var theImages = new Array();
normal_delay = 1000;
delay = normal_delay;  //delay between frames in 1/100 seconds
delay_step = 10;
delay_max = 30000;
delay_min = 1;
current_image = first_image;     //number of the current image
timeID = null;
status = 1;            // 0-stopped, 1-playing
play_mode = 1;         // 0-normal, 1-loop, 2-swing
size_valid = 0;
var loadCount = 1;
var last_image_;
var lewidth;
var leheight;

speed_text = 1;


function scalePreserveAspectRatio(imgW,imgH,maxW,maxH){
//	console.log(imgW,",",imgH,",",maxW,",",maxH);
    return(Math.min((maxW/imgW),(maxH/imgH)));
}

function naturalCompare(a, b) {
	var ax = [], bx = [];
	
	a.replace(/(\d+)|(\D+)/g, function(_, $1, $2) { ax.push([$1 || Infinity, $2 || ""]) });
	b.replace(/(\d+)|(\D+)/g, function(_, $1, $2) { bx.push([$1 || Infinity, $2 || ""]) });
	
	while(ax.length && bx.length) {
		var an = ax.shift();
		var bn = bx.shift();
		var nn = (an[0] - bn[0]) || an[1].localeCompare(bn[1]);
		if(nn) return nn;
	}
	
	return ax.length - bx.length;
}