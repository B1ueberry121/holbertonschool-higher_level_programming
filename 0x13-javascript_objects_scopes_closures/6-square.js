#!/usr/bin/node

const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let mirror = 1; mirror <= this.height; mirror++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
