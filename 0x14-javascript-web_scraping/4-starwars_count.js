#!/usr/bin/node
const args = process.argv;
const request = require('request');
let pichu = 0;
request(args[2], (err, res, body) => {
  if (err) { return console.log(err); }
  const js = JSON.parse(body);
  js.results.forEach(element => {
    element.characters.forEach(ch => {
      if (ch.includes('/18/')) { pichu = pichu + 1; }
    });
  });
  console.log(pichu);
});
