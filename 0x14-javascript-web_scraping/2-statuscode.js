#!/usr/bin/node
// script that display the status code of a GET request.

const request = require('request');

// capture url from command line
const url = process.argv[2];

// use request to send a GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    process.exit(1);
  }
  console.log('code:', response.statusCode);
});
