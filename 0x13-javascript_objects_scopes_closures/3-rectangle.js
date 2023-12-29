#!/usr/bin/node


// class Rectangle with a constructor
class Rectangle {
	constructor (w, h) {
		// ensure w/h > 0 and a number, else create empty object
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
		else {
			return {}
		}
	}
	
	print() {
		for (let i = 0; i < this.height; i++) {
			let row = '';
			for (let y = 0; y < this.width; y++) {
				row += 'x';
			}
			console.log(row);
		}
	}
}

// expose functionality of this module to other modules
module.exports = Rectangle;
