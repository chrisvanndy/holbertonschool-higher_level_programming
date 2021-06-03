#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (i, j) {
    let str = '';
    for (i = 0; i < this.width; i++) {
      str += 'X';
    }
    for (j = 0; j < this.height; j++) {
      console.log(str);
    }
  }
}
module.exports = Rectangle;
