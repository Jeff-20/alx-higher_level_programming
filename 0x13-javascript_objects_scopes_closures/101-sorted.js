#!/usr/bin/node
// Imports dictionary of occurrences by user id and computes
// a dictionary of users ids by occurrence

const dict = require('./101-data').dict;

const store = {};

for (const i in dict) {
  if (!store[dict[i]]) {
    store[dict[i]] = [];
  }
  store[dict[i]].push(i);
}

console.log(store);
