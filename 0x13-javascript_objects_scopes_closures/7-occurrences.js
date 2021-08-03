#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let pichu = 0;
  let pichula = 0;
  while (pichu < list.length) {
    if (list[pichu] === searchElement) {
      pichula++;
    }
    pichu++;
  }
  return pichula;
};
