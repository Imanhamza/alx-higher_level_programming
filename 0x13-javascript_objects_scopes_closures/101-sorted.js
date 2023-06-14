#!/usr/bin/node

const { dict } = require('./101-data.js');
// console.log(dict);

const dictionary = {};

// loop over the dict to find out the occurence
for (const [index, occur] of Object.entries(dict)) {
  if (!dictionary[occur]) {
    dictionary[occur] = [];
  }
  dictionary[occur].push(index);
}
console.log(dictionary);
