#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      this.width = null;
      this.height = null;
    } else {
       this.width = w;
       this.height = h;
      }
    }
}
