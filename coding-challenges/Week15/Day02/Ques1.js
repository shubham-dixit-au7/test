/*Question 1) - Create a for loop that iterates up to 100 while outputting "fizz" at multiples of 3, "buzz" at multiples of 5 
			  and "fizzbuzz" at multiples of 3 and 5.
*/


//Answer- JavaScript Code(File- Ques1.js)-

for (x=1; x <= 100; x++){
    if( x % 3 == 0 ){
        console.log("fizz");
    }
    if( x % 5 == 0 ){
        console.log("buzz");
    }
    if( ( x % 3 != 0 ) && ( x % 5 != 0 ) ){
        console.log("fizzbuzz");
    }
}
