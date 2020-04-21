/*
Question 1) Create a function that returns only strings with unique characters.
			Examples-
			filterUnique(["abb", "abc", "abcdb", "aea", "bbb"]) ➞ ["abc"]
			"b" occurs in "abb" more than once, "b" occurs in "abcdb" more than once, etc.
			filterUnique(["88", "999", "989", "9988", "9898"]) ➞ []
			filterUnique(["ABCDE", "DDEB", "BED", "CCA", "BAC"]) ➞ ["ABCDE", "BED", "BAC"]
*/

//Answer- 
function filterUnique(arr){
    let unique = [];
    for (let each of arr){
        if (each === each.split('').filter(function(item, i, ar){ return ar.indexOf(item) === i; }).join('')){
            unique.push(each);
        }
    }
    console.log(unique);
}
filterUnique(["abb", "abc", "abcdb", "aea", "bbb"]);
filterUnique(["88", "999", "989", "9988", "9898"]);
filterUnique(["ABCDE", "DDEB", "BED", "CCA", "BAC"]);