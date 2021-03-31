/*-----------------------------------------------------------------------------------

    Version: 1.0

-----------------------------------------------------------------------------------*/
(function ($) {
    "use strict";
    //new WOW().init();
    /*--
        Menu Sticky
    -----------------------------------*/
    
    $('.open-form').click(function(){
        $('.s_website_form').toggleClass('hidden');
        $('html, body').animate({scrollTop:$(".s_website_form").offset().top-200}, 'slow');
        return false;
    })
})(jQuery);