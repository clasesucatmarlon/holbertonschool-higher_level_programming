#!/usr/bin/node
// script that prints the addition of 2 integers

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add (valueA, valueB) {
  return valueA + valueB;
}

if (isNaN(a) || isNaN(b)) {
  console.log(NaN);
} else {
  console.log(add(a, b));
}
