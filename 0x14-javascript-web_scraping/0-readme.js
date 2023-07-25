#!/usr/bin/node
// script that reads and prints the content of a file.

const file = process.argv[2];
const fs = require('fs');

fs.readFile(file, 'utf8', (err, content) => {
  if (err) {
    console.log(err);
  } else {
    console.log(content);
  }
});
