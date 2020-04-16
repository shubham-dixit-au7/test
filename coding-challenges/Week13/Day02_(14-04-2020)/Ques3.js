/*
Question 3) -  	Find the Vowels
				This is probably one of the less challenging challenges (no pun intended) — in terms of
				difficulty — but that doesn’t detract from the fact that you could come across it during a
				job interview. It goes like this.
				Understanding the challenge
				You can state the vowels challenge as follows: write a function that takes a string as
				argument and returns the number of vowels contained in that string.
				The vowels are “a”, “e”, “i”, “o”, “u”.
				Examples:
				findVowels('hello') // --> 2
				findVowels('why') // --> 0
*/


//Answer- 
function findVowels(string){
  var count = 0;
  var vowels =["a", "e", "i", "o", "u"]
  for (let letter of string.toLowerCase()){
    if (vowels.includes(letter)) {
       count++
    }
}
return count;
}
console.log(findVowels('hello'));// --> 2
console.log(findVowels('why')); // --> 0
console.log(findVowels('The Quick Brown Fox Jumps Over The Lazy Dog')); // --> 5