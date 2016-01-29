// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-16-closest-numbers

function processData(input) {
    var a_input = input.split("\n");
    var n = Number(a_input[0]);
    var a = a_input[1].split(" ").map(Number);
    var min_diff = Number.MAX_SAFE_INTEGER;
    var differences = []; 
    
    for (var i = 0; i < a.length-1; i++) {
        for (var j = i+1; j < a.length; j++) {
            var d = Math.abs(a[i] - a[j]);
            if (d < min_diff) {
                differences.length = 0;
                min_diff = d;
                differences.push(a[i], a[j]);
            }
            else if (d == min_diff) {
                differences.push(a[i], a[j]);
            }
        }
    }
    
    console.log(differences.sort().join(' '));
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
