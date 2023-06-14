#!/usr/bin/node

// print the source array from 100-data.js As a list
const array = require('./100-data').list;
console.log(array);

let index = 0;
const mapping = array.map(function (num) {
  return (num * index++);
});
console.log(mapping);
