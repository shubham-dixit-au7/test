/*
Question- 	Write a Javascript function that takes an array and a value and search that value in the array.
			Function should take two arguments - an array and a value to search inside the array.
			If the element is found, the function should return the position of the element in an array.
			If the element is not found, the function should return "-1".
*/


//Answer-


function Search(array, value){
  for (var i=0; i<array.length; i++)
  {
    if(array[i] == value)
      return i+1;
  }
  return "-1";
}

console.log(Search([1,4,6,7],9));
