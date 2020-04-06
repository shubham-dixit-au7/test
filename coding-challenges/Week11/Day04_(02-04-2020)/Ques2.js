/*
Question 2) Write javascript program for following conditions:
1) A function  evenFunction() that returns if a number is even or not.
2) A function oddFunction() that returns if a number is odd or not.
3) A function squareFunction() that returns if a number is square or not.
*/

//Answer- 
function isEven(value) {
	if (value%2 == 0)
		return true;
	else
		return false;
}
function isOdd(value) {
  if(value%2 != 0)
    return true;
  else
    return false;
}
function isSquare(n) {
  for (var i = 0; i < n / 2 + 2; i++)
  {
    if (i * i == n)
    {
      return true;
    }
  }
  return false;
}

console.log(isEven(5));
console.log(isEven(264));
console.log(isOdd(173));
console.log(isOdd(786));
console.log(isSquare(324));
console.log(isSquare(288));