/*
Question 1) -   Implement enqueue and dequeue using only two stacks.
*/

//Answer-
var firstStack = [];
var secondStack = [];

function Enqueue(elem) {
  firstStack.push(elem);
}

function Dequeue() {
  if (secondStack.length === 0) {
    if (firstStack.length === 0)
    { return 'Queue Empty'; }
    while (firstStack.length > 0) {
      var a = firstStack.pop();
      secondStack.push(a);
    }
  }
  return secondStack.pop();
}

Enqueue('shubham');
Enqueue('shivam');
Enqueue('saksham');
Dequeue();