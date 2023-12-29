#!/usr/bin/node


// class Rectangle with a constructor
class Rectangle {
	constructor (w, h) {
		this.width = w;
		this.height = h;
	}
}

// expose functionality of this module to other modules
module.exports = Rectangle;
