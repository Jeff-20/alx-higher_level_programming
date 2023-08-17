#!/usr/bin/node
// Prints the first argument passed to it

const argFirst = process.argv[2];

if (argFirst === undefined) {
  console.log('No argument');
} else {
  console.log(argFirst);
}
