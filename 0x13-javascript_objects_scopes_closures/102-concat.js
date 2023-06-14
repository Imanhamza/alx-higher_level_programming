#!/usr/bin/node

const process = require('process');
const argu = process.argv;

const files = require('fs');

const file1 = files.readFileSync(argu[2]);
const file2 = files.readFileSync(argu[3]);

files.writeFileSync(argu[4], file1 + file2);
