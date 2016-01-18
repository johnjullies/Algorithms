// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-5-loops

function processData(input) {
    var input_a = input.split('\n');
    var T = Number(input_a[0]);
    
    for (var i = 1; i <= T; i++) {
        var _ = input_a[i].split(' ').map(Number);
        var a = _[0],
            b = _[1],
            n = _[2],
            result = [];
        
        var sum = a;
        for (j = 0; j < n; j++) {
            sum += Math.pow(2, j) * b;
            result.push(sum);
        }
        
        console.log(result.join(' '));
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
