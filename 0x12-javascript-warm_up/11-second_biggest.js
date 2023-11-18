#!/usr/bin/node

// capture command line args
const args = process.argv.slice(2);

// check no. of args
if (args.length <= 1) {
  console.log(0);
} else {
  // convert args to ints then sort them(ascending order)
  const sortedInts = args.map(Number).sort((a, b) => b - a);

  console.log(sortedInts[1]);
}
