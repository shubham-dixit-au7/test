/*
Question 2) -  	Create a function that takes an array and a string as arguments and return the index of the string.
				Examples
				findIndex(["hi", "edabit", "fgh", "abc"], "fgh") ➞ 2
				findIndex(["Red", "blue", "Blue", "Green"], "blue") ➞ 1
				findIndex(["a", "g", "y", "d"], "d") ➞ 3
				findIndex(["Pineapple", "Orange", "Grape", "Apple"], "Pineapple") ➞ 0
*/


//Answer- 
function findIndex(array, string){
  for (let i = 0; i < array.length; i++){
    if(array[i] === string){
      return i;
    }
  }
  return "Not Found";
}
console.log(findIndex(["hi", "edabit", "fgh", "abc"], "fgh")); //➞ 2
console.log(findIndex(["Red", "blue", "Blue", "Green"], "blue")); //➞ 1
console.log(findIndex(["a", "g", "y", "d"], "d")); //➞ 3
console.log(findIndex(["Pineapple", "Orange", "Grape", "Apple"], "Papaya")); //➞ "Not Found"