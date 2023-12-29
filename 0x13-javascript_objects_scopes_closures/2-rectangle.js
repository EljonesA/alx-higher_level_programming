#!/usr/bin/node


// class Rectangle with a constructor
class Rectangle {
	constructor (w, h) {
		// ensure w/h > 0, else create empty object
		if (w <= 0 || h <= 0)
		{
			return {};
		}

		this.width = w;
		this.height = h;
	}
}

// expose functionality of this module to other modules
module.exports = Rectangle;
