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

    Promise.all(movieData.characters.map(fetchCharacter))
      .then(characters => {
        characters.forEach(character => console.log(character.name));
      })
      .catch(err => {
        process.exit(1); process.exit(1);
      });
  } catch (err) {
    process.exit(1);
  }
});

// Function to fetch character details from a character URL
function fetchCharacter (characterUrl) {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }

      const characterData = JSON.parse(body);

      resolve(characterData);
    });
  });
}
