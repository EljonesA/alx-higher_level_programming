#!/usr/bin/node
//Parent class
const Square_Parent = require('./5-square.js');


// class square that inherits class Rectangle
class Square extends Square_Parent {
	constructor (size) {
		super(size);
	}

	// instance method that prints the rectangle using the character c
	charPrint (c) {
		if (c === undefined) {
			c = 'X';
		}

		for (let i = 0; i < this.height; i++) {
			let row = '';
			for (let y = 0; y < this.width; y++) {
				row += c;
			}
			console.log(row);
		}
	}
}

// make this module funnctionality accessible to other modules
module.exports = Square;
