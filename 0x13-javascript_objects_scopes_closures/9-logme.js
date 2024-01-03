#!/usr/bin/node
/*
 * Function that prints no. of args already printed followed by new arg value
 * "this" used to create/access counter variable that persits between function
 * calls.
 * The same "this"context is retained across calls within the same execution
 * context (i.e function called from same script)
*/


exports.logMe = function (item) {
	if (!this.argsPrinted) {
		this.argsPrinted = 0;
	}
	console.log(`${this.argsPrinted}: ${item}`);
	this.argsPrinted++;
}
