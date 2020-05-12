/*
1. Fetch the data from http://jsonplaceholder.typicode.com/comments
2. Create a new array but each object should contain only postId, body
3. Create a filtered array with respect to the body’s character limit to less than or equal to 50 characters.
4. Try to analyse the data, by giving a count of posts with respect to post ID.

*/

// It will fetch data only when you go to the route

const express = require('express');
const fetch = require('node-fetch');

const app = express();

app.get('/fetch',async(req,res)=>{
    try{
        const fetchedData = await fetch('http://jsonplaceholder.typicode.com/comments')
        const data = await fetchedData.json();
        let output = [] , filteredArray = [] , count = 0 , postCount = {};
        for(let i=0;i<data.length;i++){
            output.push({'postId':data[i].postId,'body':data[i].body})
            if(data[i].body.length<=50)
                filteredArray.push({'postId':data[i].postId,'body':data[i].body});
            if(!postCount[output[i].postId])
                postCount[output[i].postId] = count + 1
            else{
                postCount[output[i].postId]= postCount[output[i].postId] +1
            }
        }
        console.log(output);
        //the filtered array is empty because no data is having body.length < 50
        console.log(filteredArray);
        console.log(postCount);
        res.send('got it');
    }
    catch(error){
        console.log(res.statusCode);
        console.log(error.message);
    }
})

app.listen(8000,()=>{
    console.log('connected at '+ 8000);
})