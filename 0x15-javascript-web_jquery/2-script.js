// wait for DOM to load
$(document).ready(function () {
  $('#red_header').click(function () {
    // update text color to red
    $('header').css('color', '#FF0000');
  });
});
