/*
Question 2) -   Create a function that takes in a current mood and return a sentence in the following format: "Today, I am feeling {mood}". 
				However, if no argument is passed, return "Today, I am feeling neutral".
				Examples-
				moodToday("happy") ➞ "Today, I am feeling happy"
				moodToday("sad") ➞ "Today, I am feeling sad"
				moodToday() ➞ "Today, I am feeling neutral"
*/


//Answer-
function currentMood(mood = "Neutral") {
  console.log("Today, I am feeling " + mood);
}
  
currentMood("Happy"); // ➞ "Today, I am feeling happy"
currentMood("Sad"); // ➞ "Today, I am feeling sad"
currentMood();  // ➞ "Today, I am feeling neutral"
