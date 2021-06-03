#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;

    if (w <= 0 || w === undefined) {
      this.width = undefined;
      this.height = undefined;
    } else {
      this.width = w;
    }
    if (h <= 0 || h === undefined) {
      this.width = undefined;
      this.height = undefined;
    } else {
      this.height = h;
    }
  }
}
module.exports = Rectangle;
