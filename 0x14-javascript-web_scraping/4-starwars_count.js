#!/usr/bin/node
// script that prints the number of movies where the character
// [Wedge Antillee] is present.

const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const filmsData = JSON.parse(body).results;
    // const characterMovies = filmsData.characters
    let count = 0;
    for (let i = 0; i < filmsData.length; i++) {
      const characterMovies = filmsData[i].characters;
      for (let j = 0; j < characterMovies.length; j++) {
        if (characterMovies[j].endsWith('18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
