#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments

const list = process.argv;
list.splice(0, 2);
const len = list.length;
let value = 0;

if (len === 0 || len === 1) {
  console.log('0');
} else {
  list.sort((a, b) => a - b);
  value = list[len - 2];
  console.log(value);
}
