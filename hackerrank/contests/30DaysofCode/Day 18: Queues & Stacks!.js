// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-18-queues-stacks

function Palindrome(){
    var stack = [];
    var q = [];

    this.pushCharacter = function(ch) {
        stack.push(ch);
    };

    this.enqueueCharacter = function(ch) {
        q.push(ch);
    };
    
    this.popCharacter = function() {
        return stack.pop();
    };
    
    this.dequeueCharacter = function() {
        return q.shift();
    };
}
