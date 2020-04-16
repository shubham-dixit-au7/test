/*
Question 4) -   Create a function that takes an object argument sizes (contains width, length, height keys) and returns the volume of the 
				box.
				Examples
				volumeOfBox({ width: 2, length: 5, height: 1 }) ➞ 10
				volumeOfBox({ width: 4, length: 2, height: 2 }) ➞ 16
				volumeOfBox({ width: 2, length: 3, height: 5 }) ➞ 30
*/


//Answer- 
function volumeOfBox(sizes){
  return sizes.width * sizes.height * sizes.length;
}
console.log(volumeOfBox({ width: 2, length: 5, height: 1 })); //➞ 10
console.log(volumeOfBox({ width: 4, length: 2, height: 2 })); //➞ 16
console.log(volumeOfBox({ width: 2, length: 3, height: 5 })); //➞ 30