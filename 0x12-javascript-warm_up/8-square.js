#!/usr/bin/node
// script that prints a square

const number = parseInt(process.argv[2]);

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
}
