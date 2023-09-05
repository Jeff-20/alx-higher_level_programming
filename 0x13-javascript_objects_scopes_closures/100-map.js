#!/usr/bin/node
// Imports an array and computes a new array

let list = require('./100-data').list;
console.log(list);
list = list.map((a, c) => {
  return a * c;
});
console.log(list);
