#!/usr/bin/node
// Defines a function that converts a number
// from base 10 to another base passed as argument

exports.converter = function (base) {
  return function (a) {
    return a.toString(base);
  };
};
