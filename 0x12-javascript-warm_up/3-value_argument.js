#!/usr/bin/node
const process = require('process');

const argu = process.argv;
let len = 0;
argu.forEach((index) => {
  len = len + 1;
});
if (len === 2) {
  console.log('No argument');
} else {
  console.log(argu[2]);
}
