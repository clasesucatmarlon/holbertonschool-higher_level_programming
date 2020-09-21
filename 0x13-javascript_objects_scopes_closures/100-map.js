#!/usr/bin/node
// Write a script that imports an array and computes a new array

const list = require('./100-data.js').list;

const ar = list.map(function (x, i) {
  return x * i;
});

console.log(list);
console.log(ar);
