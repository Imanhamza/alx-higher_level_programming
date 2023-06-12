#!/usr/bin/node

const process = require('process');

const argu = process.argv;

if (parseInt(argu[2])) {
  const len = parseInt(argu[2]);
  for (let i = 0; i < len; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
