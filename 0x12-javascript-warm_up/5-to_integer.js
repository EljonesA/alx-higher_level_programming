#!/usr/bin/node

// capture first argument
const firstArg = process.argv[2];

// convert the arg to a valid integer
const convertedInt = parseInt(firstArg);

// check conversion. If successful log the number
if (!isNaN(convertedInt)) {
  console.log(`My number: ${convertedInt}`);
} else {
  console.log('Not a number');
}
