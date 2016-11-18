/**
 * Created by Alexander-Laptop on 17-Nov-16.
 * This script will have to be loaded to every page to init special functionality for the website.
 */

$(document).ready(function() {
	$('.carousel').carousel();
	$('.carousel-slider').slider({full_width: true});//slider init
    $(".button-collapse").sideNav();
    
});
