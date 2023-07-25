#!/usr/bin/node
// A script that writes a string to a file.

const file = process.argv[2];
const fs = require('fs');
const content = process.argv[3];

fs.writeFile(file, content, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
