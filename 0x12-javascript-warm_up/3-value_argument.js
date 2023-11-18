#!/usr/bin/node
const firstArg = process.argv[2]; // capture first arg

if (!firstArg) {
  console.log('No argument')
} else {
  console.log(firstArg);
}
