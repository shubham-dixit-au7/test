/*
Question 2- Given two strings, return true if they are anagrams of one another
			For example: Mary is an anagram of Army
*/

//Answer-
var anagram = (str1, str2) => str1.toLowerCase().replace(/[^a-z\d]/g,'').split('').sort().join('') === str2.toLowerCase().replace(/[^a-z\d]/g,'').split('').sort().join('');

console.log(anagram('Mary', 'Army'));   // True
console.log(anagram('Shubham', 'Shivam'));   // False