#!/usr/bin/node
// script that prints number of movies where the
// character “Wedge Antilles” is present.

const request = require('request');

// capture API url
const charId = '18';
const url = process.argv[2];

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
    const films = JSON.parse(body).results;

    const count = films.filter(film => film.characters.includes(
	    `https://swapi-api.alx-tools.com/api/people/${charId}/`)).length;

    console.log(count);
  } catch (err) {
    process.exit(1);
  }
});
