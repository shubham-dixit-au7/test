/*
Question 2) -  	A word is an anagram of another word if both use the same letters in the same quantity,
				but arranged differently.
				Understanding the challenge
				You can state this challenge in the following terms: 
				write a function that checks if two	provided strings are anagrams of each other; 
				letter casing shouldn’t matter. Also,consider only characters, not spaces or punctuation.
				For example:
				anagram('finder', 'Friend') --> true
				anagram('hello', 'bye') --> false
*/


//Answer-

var anagram = (str1, str2) => str1.toLowerCase().replace(/[^a-z\d]/g,'').split('').sort().join('') === str2.toLowerCase().replace(/[^a-z\d]/g,'').split('').sort().join('');

console.log(anagram('listen', 'Silent'));    // True
console.log(anagram('Shubham', 'Shivam'));   // False
console.log(anagram('finder', 'Friend'));    // True
console.log(anagram('hello', 'bye'));        // False