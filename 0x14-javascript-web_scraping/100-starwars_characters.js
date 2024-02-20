#!/usr/bin/node

const request = require('request');
// movie ID from command line
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(url, (error, response, body) => {
  if (error) {
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    process.exit(1);
  }

  try {
    const movieData = JSON.parse(body);
    // Extract characters' URLs from the movie data
    const characterURLs = movieData.characters;

    characterURLs.forEach(characterURL => {
      request.get(characterURL, (error, response, body) => {
        if (error) {
          return;
        }

        // Parse the character details as JSON
        const characterData = JSON.parse(body);

        // print characters
        console.log(characterData.name);
      });
    });
  } catch (err) {
    process.exit(1);
  }
});
