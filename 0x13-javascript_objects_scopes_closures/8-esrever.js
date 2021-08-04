#!/usr/bin/node

exports.esrever = function (list) {
  const result = [];
  for (let idx = list.length - 1; idx >= 0; idx--) {
    result.push(list[idx]);
  }
  return result;
};
