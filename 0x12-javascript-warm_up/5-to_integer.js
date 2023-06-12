#!/usr/bin/node
const process = require('process');

const argu = process.argv;

if (parseInt(argu[2])) {
  console.log('My number: ' + parseInt(argu[2]));
} else {
  console.log('Not a number');
}
