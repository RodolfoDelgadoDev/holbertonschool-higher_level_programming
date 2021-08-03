#!/usr/bin/node
const Scuar = require('./5-square.js');
class Square extends Scuar {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let pichu = 0; pichu < this.height; pichu++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
