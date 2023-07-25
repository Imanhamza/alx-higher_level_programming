#!/usr/bin/node
// A script that prints the title of a Star Wars movie where
// the episode number matches a given integer.

const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
