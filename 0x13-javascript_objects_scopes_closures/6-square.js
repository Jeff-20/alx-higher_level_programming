#!/usr/bin/node
// Defines a class 'Square' that inherits class
// 'Square' of 5-square.js

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      console.log(super.print());
    } else {
      let storeC = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          storeC += c;
        }
        console.log(storeC);
        storeC = '';
      }
    }
  }
}
module.exports = Square;
