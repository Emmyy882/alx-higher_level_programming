#!/usr/bin/node

let parse = parseInt(process.argv[2], 10);
if (parse) {
	console.log("My number: " + parse);
} else {
	console.log("Not a number");
}
