#!/usr/bin/node
// script that prints the title of a Star Wars movie where the
// episode number matches a given integer.

const request = require('request');

// capture Movie ID
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id + '/';

// send request
request.get(url, (error, response, body) => {
  if (error) {
    process.exit(1);
  }
  // check response status code
  if (response.statusCode !== 200) {
    process.exit(1);
  }
  // parse the data before accessing
  try {
    const movie = JSON.parse(body);

    // retrieve movie title
    const title = movie.title;
    console.log(title);
  } catch (err) {
    process.exit(1);
  }
});
