// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-17-exceptions

function Calculator() {
    this.power = function(n, p) {
        if (n >= 0 && p >= 0)
            return Math.pow(n, p);
        else 
            throw(new Error("n and p should be non-negative").message);
    }
}
