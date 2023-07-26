#!/usr/bin/node
// A script that prints all characters of a Star Wars movie:

const request = require('request');
const mId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${mId}/`;
// console.log(apiUrl);
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const movieData = JSON.parse(body);
  const chars = movieData.characters;
  
  // console.log(movieData);
  for (const chr of chars) {
    request.get(chr, (error, response, body) => {
      console.log((JSON.parse(body)).name);
    });
  }
});
