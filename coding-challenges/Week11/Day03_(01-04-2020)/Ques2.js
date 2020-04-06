/*
Question2- Write a JavaScript program to sort the items of an array.
Sample array :  var arr1 = [ 3, 8, 7, 6, 5, -4, 3, 2, 1 ];
Sample Output : [ -4,3,1,2,3,5,6,7,8]
*/


//Answer-
var array=[-3,8,7,6,5,-4,3,2,1];
var blankArray=[];
var min=array[0];
var pos;
var max=array[0];
for (i=0; i<array.length; i++)
{
        if (max<array[i]) 
        {
        max=array[i];
        }
}

for (var i=0;i<array.length;i++)
{
        for (var j=0;j<array.length;j++)
        {
                if (array[j]!="x")
                {
                        if (min>array[j]) 
                        {
                                min=array[j];
                                pos=j;
                        }
                }
        }
        blankArray[i]=min;
        array[pos]="x";
        min=max;
}
console.log(blankArray);
