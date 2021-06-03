#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;

    if (w <= 0 || w === undefined) {
      this.width = 0;
      this.height = 0;
    } else {
      this.width = w;
    }
    if (h <= 0 || h === undefined) {
      this.width = 0;
      this.height = 0;
    } else {
      this.height = h;
    }
  }
}
module.exports = Rectangle;
