#!/usr/bin/node
let elem = 2;
while (elem < process.argv.length) {
  console.log(process.argv[elem]);
  elem = elem + 1;
}
