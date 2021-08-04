#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let idx = 0; idx < process.argv[2]; idx++) {
    let str = '';
    for (let idx2 = 0; idx2 < process.argv[2]; idx2++) {
      str += 'X';
    }
    console.log(str);
  }
}
