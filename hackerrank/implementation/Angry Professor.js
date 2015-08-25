// https://www.hackerrank.com/challenges/angry-professor

function processData(input) {
    var inputArray = input.split("\n");
    var parse_fun = function(s) {return parseInt(s, 10); }
    var line = 1;
    for (var test = 1; test <= parse_fun(inputArray[0]); test++) {
        var k = parse_fun(inputArray[line].split(" ")[1]);
        line++;
        var log = inputArray[line].split(" ").map(Number);
        var notLate = 0;
        for (var j = 0; j < log.length; j++) {
            if (log[j] <= 0) notLate++;
        }
        if (notLate >= k) console.log("NO");
        else console.log("YES");
        line++;
    }
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
