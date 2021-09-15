#!/usr/bin/node
const args = process.argv;
const request = require('request');
const dict = {};
request(args[2], (err, res, body) => {
  if (err) { return console.log(err); }
  const js = JSON.parse(body);
  js.forEach(element => {
    const key = element.userId;
    if (element.completed === true) {
      if (!(key in dict)) {
        dict[key] = 1;
      } else {
        dict[key] += 1;
      }
    }
  });
  console.log(dict);
});
