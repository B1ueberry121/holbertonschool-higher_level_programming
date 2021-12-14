#!/usr/bin/node

const argv = require('process').argv;
let square = '';

if (isNaN(parseInt(argv[2]))) {
  console.log('Missing size');
} else if (parseInt(argv[2])) {
  for (let row = 1; row <= parseInt(argv[2]); row++) {
    for (let col = 1; col <= parseInt(argv[2]); col++) {
      square += 'X';
    }
    console.log(square);
    square = '';
  }
}
