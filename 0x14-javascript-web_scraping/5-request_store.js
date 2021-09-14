#!/usr/bin/node
const args = process.argv;
const request = require('request');
const fs = require('fs');
request(args[2], (err, res, body) => {
  if (err) { return console.log(err); }
  fs.writeFile(args[3], body, 'utf8', (err, data) => {
    if (err) {
      console.log(err);
    }
  });
});
