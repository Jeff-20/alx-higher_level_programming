#!/usr/bin/node
// Increments and calls a function

exports.addMeMaybe = function (number, theFunction) {
  number = number + 1;
  theFunction(number);
};
