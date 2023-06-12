#!/usr/bin/node

const process = require('process');
const argu = process.argv;

const num = [];
for (let i = 2; i < argu.length; i++) {
  num.push(parseInt(argu[i]));
}
console.log(Math.max(...num));
