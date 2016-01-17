// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-1-data-types

function processData(input) {
    console.log('Primitive : double');
    console.log('Primitive : char');
    console.log('Primitive : boolean');
    console.log('Primitive : int');
    console.log('Referenced : String');
    console.log('Primitive : boolean');
    console.log('Primitive : double');
    console.log('Primitive : char');
    console.log('Referenced : String');
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
