/*Question1-Create a function that returns the number of argument it was called with.
			Examples-
			numArgs() ➞ 0
			numArgs("foo") ➞ 1
			numArgs("foo", "bar") ➞ 2
			numArgs(true, false) ➞ 2
			numArgs({}) ➞ 1
*/


//Answer- 
function numArgs() { 
var i = arguments.length; 
return i;
}


console.log(numArgs());
console.log(numArgs("foo"));
console.log(numArgs("foo", "bar"));
console.log(numArgs(true, false));
console.log(numArgs({}));