#!/usr/bin/node

const argv = require('process').argv;

let num1 = argv.slice(2);
num1 = num1.sort();

function sndMaxInt (num1) {
  if (num1.length < 2) {
    return 0;
  } else {
    num1.pop();
    return num1.pop();
  }
}

console.log(sndMaxInt(num1));
