/*
Question 5) -	Write a function that validates whether two strings are identical. Make it case insensitive.
				Examples-
				match("hello", "hELLo") ➞ true
				match("motive", "emotive") ➞ false
				match("venom", "VENOM") ➞ true
				match("mask", "mAskinG") ➞ false
*/


//Answer-
function match(var1, var2){
  if (var1.toLowerCase() == var2.toLowerCase())
    return true;
  return false;
}


console.log(match("hello", "hELLo")); //➞ true
console.log(match("motive", "emotive")); //➞ false
console.log(match("venom", "VENOM")); //➞ true
console.log(match("mask", "mAskinG")); //➞ false