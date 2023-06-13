#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      let line = '';
      for (let j = 0; j < this.height; j++) {
        if (c) {
          line += c;
        } else {
          line += 'X';
        }
      }
      console.log(line);
    }
  }
}
module.exports = Square;
