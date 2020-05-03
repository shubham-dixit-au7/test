/*
Question-   ES6 Classes
			Build an object oriented sort of connection between a Fruit and an Apple.
			Every fruit should have the name, color properties and methods naming ripe, grow.
			The Apple fruit should have properties of type, variety and also all other additional methods. Any sort of Object oriented model is fine.

*/



//Answer-
class Fruit{
	constructor (name ,color) {
		this.name = name;
		this.color = color;
	}	
  grow(){
    return this.name + " is grown now.";
  }
  ripe(){
    return this.name + " is rippen and " + this.color + " in color."
  }
}

class Apple extends Fruit{
  constructor(){
    super("Apple", "Red");
  }
  variety = 'Kashmiri';
  type = 'Fresh';

  cost(){
    return this.variety + " " + this.type + " Apple is very costly."
  }
}

class Mango extends Fruit{
  constructor(){
    super("Mango", "Yellow")
  }
}

let apple = new Apple();
console.log(apple.grow());
console.log(apple.ripe());
console.log(apple.cost());


let mango = new Mango();
console.log(mango.grow());
console.log(mango.ripe());