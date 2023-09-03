#!/usr/bin/node
// Defines a class 'Square' that inherits 'Rectangle'
// of 4-rectangle.js

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
