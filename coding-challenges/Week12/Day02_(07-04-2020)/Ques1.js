/*
Question- Write a function to remove duplicates from an array.

Sample input- [1,2,3,4,3,2,1]
Sample output - [1,2,3,4]
*/

//Answer-
var removeDuplicates = (arr) => [...new Set(arr)];

console.log(removeDuplicates([1,2,3,4,3,2,1])); // [ 1, 2, 3, 4 ]
