// wait for DOM to load
$(document).ready(function () {
  // add click event listener to div with id add_item
  $('#add_item').click(function () {
    // create a new <li> element
    const newItem = $('<li>Item</li>');
    // append the nwe element to UL with class my_list
    $('ul.my_list').append(newItem);
  });
});
