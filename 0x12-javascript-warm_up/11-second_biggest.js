#!/usr/bin/node
const args = process.argv;
if (isNaN(args[3])) {
  console.log(0);
} else {
  let pichu = 2;
  let max = parseInt(args[2]);
  let secmax = parseInt(args[3]);
  while (!isNaN(args[pichu])) {
    if (max < parseInt(args[pichu])) {
      secmax = max;
      max = parseInt(args[pichu]);
    } else if (secmax < parseInt(args[pichu])) {  
        if (max == parseInt(args[pichu])){
          pichu++;
          continue;
        }
        secmax = parseInt(args[pichu]);
      }
      pichu++;
  }
  console.log(secmax);
}
