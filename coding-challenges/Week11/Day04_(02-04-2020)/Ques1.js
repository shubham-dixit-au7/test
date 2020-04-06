/*
Question 1) Write a Javascript program that produces a star pattern likes this.
*
**
***
****
*****
****
***
**
*

*/


//Answer-

var x,y,chr='';
for(x=1; x <=5; x++)
{
   for (y=0; y < x; y++)
    {
    chr=chr+("*");        
    }
 console.log(chr);
 chr='';    
}
for(x=6; x <=9; x++)
{
  for (y=10; y > x; y--)
  {
  chr=chr+("*");
  }
  console.log(chr);
  chr='';
}


