#!/usr/bin/node
const process = require('process');

const argu = process.argv.length;
if (argu === 2) {
  console.log('No argument');
} else if (argu === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
