#!/usr/bin/node

const process = require('process');
const argu = process.argv;

function factorial (a) {
  if (a === 0 || a === 1 || isNaN(a)) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
console.log(factorial(argu[2]));
