#!/usr/bin/node
const args = process.argv;
const request = require('request');
request(args[2], (err, res, body) => {
  if (err) { return console.log(err); }
  console.log('code ' + res.statusCode);
});
