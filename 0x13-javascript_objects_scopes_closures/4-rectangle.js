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
	
	// instance method that prints the rectangle using the character X
	print() {
		for (let i = 0; i < this.height; i++) {
			let row = '';
			for (let y = 0; y < this.width; y++) {
				row += 'X';
			}
			console.log(row);
		}
	}

	// instance method that exchanges the w and the h of the rectangle
	rotate() {
		let temp = this.width;
		this.width = this.height;
		this.height = temp;
	}

	// instance method that multiples the w and the h of the rectangle by 2
	double() {
		this.width = this.width * 2;
		this.height = this.height * 2;
	}
}

// expose functionality of this module to other modules
module.exports = Rectangle;
