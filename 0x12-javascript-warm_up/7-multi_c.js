#!/usr/bin/node

// capture first argument
const firstArg = process.argv[2];

// convert the arg to a valid integer
const convertedInt = parseInt(firstArg);

// check conversion. If successful log the number
if (!isNaN(convertedInt)) {
  for (let i = 0; i < convertedInt; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Not a number');
}
