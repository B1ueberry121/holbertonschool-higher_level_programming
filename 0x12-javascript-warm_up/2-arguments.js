#!/usr/bin/node

let myArgv = process.argv.slice(2);
if (myArgv.length === 0) {
console.log('No argument');
}
else if (myArgv.length === 1) {
console.log('Argument found');
}
else if (myArgv.length > 0) {
console.log('Arguments found');
}
