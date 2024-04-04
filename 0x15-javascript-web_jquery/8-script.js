// wait for DOM to load
$(document).ready(function () {
  // GET request to API
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // loop through each movie in response
    data.results.forEach(function (movie) {
      // extract movie title
      const title = movie.title;
      // create new list wuith movie title
      const listItem = $('<li>').text(title);
      // append new list item to ul with id list_movies
      $('#list_movies').append(listItem);
    })
  });
});
