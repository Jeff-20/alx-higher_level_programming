#!/usr/bin/node
// contains 'Rectangle' class that defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        console.log('X');
        if (j = this.width - 1) {
          console.log(\n);
        }
      }
    }
  }
}
module.exports = Rectangle;
