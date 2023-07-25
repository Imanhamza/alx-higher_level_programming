#!/usr/bin/node
// A script that display the status code of a GET request.

const url = process.argv[2];
const req = require('request');

req.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
