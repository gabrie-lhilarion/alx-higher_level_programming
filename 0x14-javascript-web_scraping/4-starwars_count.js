const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    return;
  }

  const films = JSON.parse(body).results;
  const characterId = '18';
  const numMoviesWithWedge = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)).length;

  console.log(numMoviesWithWedge);
});
