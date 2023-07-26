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
  
  let count = 0;
  for (let i = 0; i < chars.length; i++) {
    request.get(chars[i], (error, response, body) => {
      if (error) {
        console.log(error);
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
}
);
