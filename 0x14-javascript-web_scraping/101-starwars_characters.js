#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const request = require('request');
const mId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${mId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const movieData = JSON.parse(body);
  const chars = movieData.characters;

  getChar(chars, 0);
});

// Function to get the index of each character
function getChar (chr, index) {
  request(chr[index], (error, respose, body) => {
    if (error) {
      console.log(error);
    }

    console.log(JSON.parse(body).name);
    if (index + 1 < chr.length) {
      getChar(chr, index + 1);
    }
  });
}
