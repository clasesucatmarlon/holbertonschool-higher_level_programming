#!/usr/bin/node
/* script that imports a dictionary of occurrences by
user id and computes a dictionary of user ids by occurrence. */

const dict = require('./101-data.js').dict;

const d = {};

for (const k in dict) {
  if (d[dict[k]] === undefined) {
    d[dict[k]] = [];
  }
  d[dict[k]].push(k);
}
console.log(d);
