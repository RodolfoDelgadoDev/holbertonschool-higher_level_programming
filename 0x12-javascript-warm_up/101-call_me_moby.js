#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let pichu = 0; pichu < x; pichu++) {
    theFunction();
  }
};
