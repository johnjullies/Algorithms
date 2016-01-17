// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-4-boolean-operators-class-vs-instance

function Person(initial_age) {
  if (initial_age < 0) {
    console.log("This person is not valid, setting age to 0.");
    this.age = 0;
  }
  else 
    this.age = initial_age;

  this.amIOld = function() {
    if (this.age < 13)
      console.log("You are young.");
    else if (this.age >= 13 && this.age < 18)
      console.log("You are a teenager.");
    else 
      console.log("You are old.");
  };
	 
	this.yearPasses = function() {
	  this.age++;
	};
}
