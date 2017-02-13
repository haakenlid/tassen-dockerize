const $ = require('jquery');
require('slick-carousel/slick/slick');
require('foundation-sites/dist/js/foundation');
require('foundation-sites/dist/js/plugins/foundation.reveal');

$(document).foundation();
$(function(){
  $('.slideshow').slick({ dots:true, arrows:true });
});
