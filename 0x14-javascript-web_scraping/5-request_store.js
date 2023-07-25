#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file.

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request.get({ url, encoding: null }, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = body.toString('utf-8');
    fs.writeFile(filePath, content, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      } else {
        console.log(`Webpage content saved to file: ${filePath}`);
      }
    });
  }
});
