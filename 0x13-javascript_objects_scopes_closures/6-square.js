#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
