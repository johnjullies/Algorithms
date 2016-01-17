// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-0-print-hello-world

function processData(input) {
    console.log("Hello World.\nWelcome to 30 Days of Code.");
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
