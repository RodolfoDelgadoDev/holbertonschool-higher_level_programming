#!/usr/bin/node
const args = process.argv;
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + args[2];
request(url, (err, res, body) => {
  if (err) { return console.log(err); }
  const js = JSON.parse(body);
  console.log(js.title);
});
