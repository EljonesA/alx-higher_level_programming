#!/usr/bin/node

// Capture first and second command-line args
const firstArg = process.argv[2];
const secondArg = process.argv[3];

// concatenate the strings
const concatString = firstArg + ' is ' + secondArg;

// print the result
console.log(concatString);
