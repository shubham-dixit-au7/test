/*
Question 4) -   Write a function that takes an integer and:
				If the number is a multiple of 3, return "Hello".
				If the number is a multiple of 5, return "World".
				If the number is a multiple of both 3 and 5, return "Hello World".
				Examples
				helloWorld(3) ➞ "Hello"
				helloWorld(5) ➞ "World"
				helloWorld(15) ➞ "Hello World"
*/

//Answer- 
function helloWorld(val){
  if (val % 15 === 0)
    return "Hello World";
  else if (val % 5 === 0)
    return "World";

  else if (val % 3 === 0 )
    return "Hello";
}
console.log(helloWorld(3)); //➞ "Hello"
console.log(helloWorld(5)); //➞ "World"
console.log(helloWorld(15)); //➞ "Hello World"