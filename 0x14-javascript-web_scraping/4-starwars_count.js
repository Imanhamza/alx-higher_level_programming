#!/usr/bin/node
// script that prints the number of movies where the character
// “Wedge Antilles” is present.

const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const filmsData = JSON.parse(body).results;
    const characterMovies = filmsData.filter((film) =>
      film.characters.some((character) => character.endsWith('/18/'))
    );
    console.log(characterMovies.length);
  }
});
