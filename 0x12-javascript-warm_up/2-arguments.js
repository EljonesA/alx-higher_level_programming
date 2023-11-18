#!/usr/bin/node
const myArgs = process.argv.length; // check number of command-line args

if (myArgs === 2) {
  console.log('No argument');
} else if (myArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
