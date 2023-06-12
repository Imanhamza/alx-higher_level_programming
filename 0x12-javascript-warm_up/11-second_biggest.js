#!/usr/bin/node

const process = require('process');
const argu = process.argv;

const num = [];
if (argu.length === 3 || argu.length < 3) {
  console.log(0);
} else if (argu.length > 3) {
  // const num = [];
  for (let i = 2; i < argu.length; i++) {
    num.push(parseInt(argu[i]));
  }
}
const index = num.length - 1;
const sortedNum = num.sort();
// console.log(sortedNum);
console.log(sortedNum[index - 1]);
