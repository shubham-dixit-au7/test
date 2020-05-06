/*
Question 3)-Have the function LargestPair(num) take the num parameter being passed and determine the largest double digit 
			number within the whole number. For example: if num is 4759472 then your program should return 94 because that is the largest double digit number. The input will always contain at least two positive digits.

*/

//Answer- JavaScript Code(File- Ques3.js)-

function largestPair(x) {
  if(x > 9 ){
    var arr = x.toString().split('')
    var dgt = 0
    var tst = 0
    var largest = 0
    
    for (var i = 0; i < arr.length - 1; i++) {
      if (parseInt(arr[i]) >= dgt) {
        tst = parseInt(arr[i] + arr[i+1])
          if (tst > largest) { 
            largest = tst; 
          }
      }
      
    }
    return largest
  }
  else
    return "Atleast Two Digit Number Needed"
}

console.log(largestPair(4759472));
console.log(largestPair(489));
console.log(largestPair(7));