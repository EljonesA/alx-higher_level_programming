// GET request to API
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  // extrat translation of "hello"
  const helloTrans = data.hello;
  // update text of div with id hello
  $('#hello').text(helloTrans);
});
