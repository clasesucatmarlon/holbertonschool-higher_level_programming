#!/usr/bin/node
// determinate factorial of a number

const number = parseInt(process.argv[2]);

function factorial (num) {
  if (isNaN(num) || num === 1 || num === 0) {
    return 1;
  }
  return factorial(num - 1) * num;
}

console.log(factorial(number));
