#!/usr/bin/node
// script that writes a string to a file.

const fs = require('fs');

// capture command line args
const args = process.argv;
const filePath = args[2];
const content = args[3];

// write content to file
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err); // print error incase of any
    process.exit(1); // non-zero value exit to indicate error
  }
});
