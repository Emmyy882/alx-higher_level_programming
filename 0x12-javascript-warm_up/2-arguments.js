#!/usr/bin/node
let argCnt = process.argv.length - 2;

if (argCnt < 1) {
	console.log("No argument");
} else if (argCnt === 1) {
	console.log("Argument found");
} else {
	console.log("Arguments found");
}
