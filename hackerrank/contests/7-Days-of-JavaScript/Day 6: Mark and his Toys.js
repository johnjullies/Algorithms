// https://www.hackerrank.com/contests/7days-javascript/challenges/mark-and-toys-2-js-only

function processData(input) {
    var _input = input.split('\n');
    var budget = Number(_input[0].split(' ')[1]);
    var toy_prices = _input[1].split(' ').map(Number).sort(function(a,b){return a-b;});
    var len = toy_prices.length;
    var result = 0;
    
    while (budget >= 0) {
        budget -= toy_prices[result];
        result++;
    }
    
    console.log(result-1);
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
