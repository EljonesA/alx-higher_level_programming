#!/usr/bin/node


// class Rectangle with a constructor
class Rectangle {
	constructor (w, h) {
		// ensure w/h > 0 and a number, else create empty object
		if (w <= 0 || !Number.isInteger(w) || h <= 0 || !Number.isInteger(h))
		{
			return {};
		}

		this.width = w;
		this.height = h;
	}
}

// expose functionality of this module to other modules
module.exports = Rectangle;
