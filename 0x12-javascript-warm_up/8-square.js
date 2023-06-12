#!/usr/bin/node

const process = require('process');

const argu = process.argv;

if (parseInt(argu[2])) {
  const len = parseInt(argu[2]);
  for (let i = 0; i < len; i++) {
    let line = '';
    for (let j = 0; j < len; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
