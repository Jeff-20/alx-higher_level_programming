#!/usr/bin/node
// Prints first argument converted to integer,preceded by 'My number:'

const firstArgInt = parseInt(process.argv[2]);
if (isNaN(firstArgInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + firstArgInt);
}
