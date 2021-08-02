#!/usr/bin/node
const num = process.argv[2];
const check = parseInt(num);
let pichu = 0;
if (num) {
  if (!isNaN(check)) {
    while (pichu < num) {
      console.log('C is fun');
      pichu = pichu + 1;
    }
  }
} else {
  console.log('Missing number of occurrences');
}
