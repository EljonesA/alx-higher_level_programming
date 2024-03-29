#!/usr/bin/node
// script that reads and prints the content of a file.

const fs = require('fs');

// fetch filepath from command line
const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log(data);
});
