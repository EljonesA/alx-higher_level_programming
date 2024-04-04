// wait for DOM to load
$(document).ready(function () {
  // GET request to API
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // extract character name
    const charName = data.name;
    // update text of div with id character
    $('#character').text(charName);
  });
});
