#!/usr/bin/node
/* function that counts the number of occurrences of an item in a list
   - exports is a special object in Node.js that allows you to expose functions,
     variables & objects to be used in other files
*/


exports.nbOccurences = function (list, searchElement) {
	if (list.includes(searchElement)) {
		let count = 0;
		for (let i = 0; i < list.Length; i++) {
			if (list[i] === searchElement) {
				count++;
			}
		}
		return count;
	}
	else {
		console.log("Search element not in the list!");
	}
}
