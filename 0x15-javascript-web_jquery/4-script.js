// wait for DOM to load
$(document).ready(function () {
  // add click event listener to div with id toggle_header
  $('#toggle_header').click(function () {
    // toggle class of header btwn red & green
    $('header').toggleClass('red green');
  });
});
