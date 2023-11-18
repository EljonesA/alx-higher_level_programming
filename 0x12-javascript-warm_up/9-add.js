#!/usr/bin/node

// add function
function add (a, b) {
  return a + b;
}

// capture first argument
const firstArg = process.argv[2];
const secondArg = process.argv[3];

// convert the arg to a valid integer
const convertedFirstArg = parseInt(firstArg);
const convertedSecondArg = parseInt(secondArg);

// check conversion. If successful add the numbers
if (!isNaN(convertedFirstArg) && !isNaN(convertedSecondArg)) {
  console.log(add(convertedFirstArg, convertedSecondArg));
} else {
  console.log('NaN');
}
