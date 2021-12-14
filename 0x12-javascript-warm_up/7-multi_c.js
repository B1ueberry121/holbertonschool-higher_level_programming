#!/usr/bin/node

const argv = require('process').argv;

if (isNaN(parseInt(argv[2]))) {
  console.log('Missing number of ocurrences');
} else if (parseInt(argv[2])) {
  for (let idx = 1; idx <= parseInt(argv[2]); idx++) {
    console.log('C is fun');
  }
}
