// Set timeout for alert box
$(function () {
    setTimeout(function () {
        $("#alert").alert("close");
    }, 2000);
});

// Add and remove active class from links
$(document).ready(function () {
    $('.category').click(function () {
        $('.category').removeClass('active');
        $(this).addClass('active');
    });
});