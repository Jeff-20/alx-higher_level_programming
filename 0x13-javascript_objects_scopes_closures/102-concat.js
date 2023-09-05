#!/usr/bin/node
// This script concatenates teo files

const fs = require('fs');

try {
  [process.argv[2], process.argv[3]].forEach((f) => {
    fs.readFileSync(f).toString().trim().split('\n').forEach((line) => {
      fs.appendFileSync(process.argv[4], line.toString() + '\n');
    });
  });
} catch (err) {
  console.log(err);
}
