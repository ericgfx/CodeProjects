$(function(){
    $(window).scroll(function() {              
        ($(document).scrollTop() + $(window).height()) / $(document).height() > 0.3 ? $('#sticky').fadeIn() : $('#sticky').fadeOut();
    });
})
