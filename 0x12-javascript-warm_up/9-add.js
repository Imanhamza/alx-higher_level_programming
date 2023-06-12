#!/usr/bin/node

const process = require('process');
const argu = process.argv;

function add (a, b) {
  const sum = parseInt(a) + parseInt(b);
  console.log(sum);
}
add(argu[2], argu[3]);
