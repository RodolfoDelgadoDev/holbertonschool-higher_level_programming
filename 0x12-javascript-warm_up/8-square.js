#!/usr/bin/node
const num = process.argv[2];
if (!num || isNaN(num)) {
  console.log('Missing size');
} else {
  for (let pichu = 0; pichu < num; pichu++) {
    console.log('X'.repeat(num));
  }
}
