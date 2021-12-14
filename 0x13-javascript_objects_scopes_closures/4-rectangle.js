#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let xh = 0; xh < this.height; xh++) {
      for (let xw = 0; xw < this.width; xw++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }

  rotate () {
    const sizeBuff = this.width;
    this.width = this.height;
    this.height = sizeBuff;
  }

  double () {
    this.height = this.height * 2;
    this.wiidth = this.width * 2;
  }
}

module.exports = Rectangle;
