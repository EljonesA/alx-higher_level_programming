// wait for DOM to load
$(document).ready(function () {
  // add click event listeer to div with red header
  $('#red_header').click(function () {
    // add class red to the header
    $('header').addClass('red');
  });
});
