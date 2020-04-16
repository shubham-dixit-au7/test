/*
Question 2) -  	Write a function fib() that takes an integer n and return the nth Fibonacci number.
*/

//Answer- 

function fib(n) {
  let a1 = [0, 1];

  if (n <= 2) return 1;

  for (let i = 2; i <= n; i++) {
    a1[i] = a1[i - 1] + a1[i - 2];
    // a1.push(a1[i-1] + a1[i-2])
  }

  return a1[n];
  // return a1
}

fib(7);