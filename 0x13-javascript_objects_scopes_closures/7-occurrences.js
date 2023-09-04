#!/usr/bin/node
// Defines a function 'nbOccurences' that returns
// the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const i in list) {
    if (searchElement === list[i]) {
      count += 1;
    }
  }
  return count;
};
