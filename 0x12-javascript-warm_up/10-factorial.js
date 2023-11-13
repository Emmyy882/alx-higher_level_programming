#!/usr/bin/node

let num = parseInt(process.argv[2]);
function factorial (num) {
	if (!num) {
		return 1;
	} else {
		if (num === 0 || num === 1) {
			return 1; //Base Case
		}
		return (num * factorial(num - 1));
	}
}
let result = factorial(num);
console.log(result);
