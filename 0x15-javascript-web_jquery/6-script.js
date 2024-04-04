// wait for DOM to load
$(document).ready(function () {
  // add click event listener to div with id update_header
  $('#update_header').click(function () {
    // update text of header element
    $('header').text('New Header!!!');
  });
});
