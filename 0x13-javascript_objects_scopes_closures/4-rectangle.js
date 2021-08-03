#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let pichu = 0; pichu < this.height; pichu++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    this.width = this.height;
    this.height = this.width;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
