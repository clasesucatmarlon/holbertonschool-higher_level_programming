#!/usr/bin/node
// script that concats 2 files

const fs = require('fs');

const f1 = fs.readFileSync(process.argv[2]);
const f2 = fs.readFileSync(process.argv[3]);
const f3 = f1 + '\n' + f2;

fs.writeFile(process.argv[4], f3, function (err) {
  // If an error occurred, show it and return
  if (err) {
    return console.error(err);
  }
});
