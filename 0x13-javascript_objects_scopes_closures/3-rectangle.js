#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (w = 0; w < this.width; w++)
      for(h = 0; h < this.height; h++)
        console.log('X');
  }
}
module.exports = { Rectangle, print};