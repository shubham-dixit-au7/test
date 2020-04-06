/*Question 1) Write a javascript program that prints even numbers from 1 to 100 in descending order.
the output should show: 
100
98
96
.
.
2
*/

//Answer-

for(i=100; i>1; i--){
if(i % 2 == 0){
    console.log(i);
  }
}

