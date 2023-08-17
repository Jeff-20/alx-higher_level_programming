#!/usr/bin/node
// searches for second biggest int in the arguments list and prints it

const args = process.argv.slice(2).map((x) => {
  return parseInt(x);
});

if (args.length <= 1) {
  console.log(0);
} else {
  console.log(args.sort((a, b) => {
    return b - a;
  })[1]);
}
