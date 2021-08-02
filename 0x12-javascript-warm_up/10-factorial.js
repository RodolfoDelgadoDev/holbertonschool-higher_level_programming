#!/usr/bin/node
function fautismo (num) {
  if (num === 0) {
    return 1;
  } else {
    return num * fautismo(num - 1);
  }
}
console.log(fautismo(isNaN(process.argv[2])));
