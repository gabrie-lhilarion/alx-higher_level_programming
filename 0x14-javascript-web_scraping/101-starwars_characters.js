#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie details. Status code: ${response.statusCode}`);
    return;
  }

  const movie = JSON.parse(body);
  const charactersUrls = movie.characters;

  // Helper function to fetch character names and print them
  const fetchAndPrintCharacters = (urls, index) => {
    if (index >= urls.length) {
      return;
    }

    const characterUrl = urls[index];
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Failed to fetch character details. Status code: ${response.statusCode}`);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);

      // Fetch and print next character recursively
      fetchAndPrintCharacters(urls, index + 1);
    });
  };

  // Start fetching and printing characters
  fetchAndPrintCharacters(charactersUrls, 0);
});
