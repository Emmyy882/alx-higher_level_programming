#!/usr/bin/node

const num = parseInt(process.argv[2]);
if (num) {
  for (let i = 0; i < num; i++) {
	  console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
