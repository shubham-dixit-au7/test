/*
Question 2) - There is an array with some numbers. All numbers are equal except for one. Try to find it!
			  Example-
				findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
				findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
*/


//Answer- JavaScript Code(File- Ques2.js)-

function findUniq(arr){
  let n, q, sum = 0;
  var len = arr.length;

  for (let i=0;i<len;i++){
    sum +=arr[i];
  }
  if(arr[0] === arr[1]){
    n=arr[0];
    q = sum - n * (len-1)
  }
  else if(arr[0] != arr[1]){
    if(arr[0] === arr[2]){
      q = arr[1];
    }
    else
      q = arr[0] 
  }
  return q;
}

console.log(findUniq([ 1, 1, 1, 2, 1, 1 ])); //=== 2
console.log(findUniq([ 0, 0, 0.55, 0, 0 ])); //=== 0.55