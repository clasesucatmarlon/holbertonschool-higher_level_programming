#!/usr/bin/node
// Write a function that returns the reversed version of a list

exports.esrever = function (list) {
  let long = list.length - 1;

  for (let i = 0; i < long; i++, long--) {
    const swap = list[i];
    list[i] = list[long];
    list[long] = swap;
  }
  return list;
};
