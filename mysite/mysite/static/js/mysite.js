$(function() {
    $('.intro').mouseover(function(){
        $('.abs-text-container p').fadeIn(500);
        $('.logo img').addClass('blur');
    });
    $('.intro').mouseleave(function(){
        $('.abs-text-container p').fadeOut(500);
        $('.logo img').removeClass('blur');
    });
});
