/*
Question 3) -  	Write a function to check if an array contains a particular number.
				Examples
				check([1, 2, 3, 4, 5], 3) ➞ true
				check([1, 1, 2, 1, 1], 3) ➞ false
				check([5, 5, 5, 6], 5) ➞ true
				check([], 5) ➞ false
*/


//Answer-
function check(array, val){
  for (let i = 0; i < array.length; i++){
    if(array[i] === val){
      return true;
    }
  }
  return false;
}
console.log(check([1, 2, 3, 4, 5], 3)); //➞ true
console.log(check([1, 1, 2, 1, 1], 3)); //➞ false
console.log(check([5, 5, 5, 6], 5)); //➞ true
console.log(check([], 5)); //➞ false