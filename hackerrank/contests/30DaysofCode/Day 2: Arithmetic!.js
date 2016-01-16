// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-2-arithmetic

function processData(input) {
    var inputArr = input.split('\n').map(function(i) {return Number(i)});
    var M = inputArr[0],
        T = inputArr[1],
        X = inputArr[2];
    
    T = (T*M)/100;
    X = (X*M)/100;
    var finalPrice = Math.round(M + T + X); 
    
    return "The final price of the meal is $"+finalPrice+"."
} 
process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   console.log(processData(_input));
});
