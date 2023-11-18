#!/usr/bin/node

// function to calculate the factorial
function factorial(n) {
  if (isNaN(n) || n < 0) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

// capture the first argument
const input = parseInt(process.argv[2]);

//compute & print the factorial
console.log(factorial (input));
