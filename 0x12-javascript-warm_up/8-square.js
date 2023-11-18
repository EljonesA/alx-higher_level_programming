#!/usr/bin/node

// capture first argument
const firstArg = process.argv[2];

// convert the arg to a valid integer
const size = parseInt(firstArg);

// check conversion. If successful log the number
if (!isNaN(size)) {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      let row = '';
      for (let j = 0; j < size; j++) {
        row += 'X';
      }
      console.log(row);
     }
  } else {
    console.log(''); // print empty line for non-positive sizes
  }
} else {
  console.log('Missing size');
}
