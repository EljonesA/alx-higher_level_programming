#!/usr/bin/node


// class square that inherits class Rectangle
class Square extends Rectangle {
	constructor (size) {
		super(size, size); // calling constructor of Rectangle
	}
}

// make this module funnctionality accessible to other modules
module.exports = Square;
