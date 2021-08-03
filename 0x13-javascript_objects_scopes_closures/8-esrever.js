#!/usr/bin/node
exports.esrever = function (list) {
  let pichu = list.length - 1;
  const arr = [];
  while (pichu !== -1) {
    arr.push(list[pichu]);
    pichu--;
  }
  return arr;
};
