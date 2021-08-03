#!/usr/bin/node

const myArgv = process.argv[2];

if (myArgv === undefined) {
  console.log('No argument');
} else {
  console.log(myArgv);
}
