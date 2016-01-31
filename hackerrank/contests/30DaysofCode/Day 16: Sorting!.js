// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-16-closest-numbers

function processData(input) {
    var a = input.split('\n');
    var myArray = a[1].split(' ').map(Number);
    myArray.sort(function(a,b){return a - b});
    var result = []
    var diff = Infinity;
    for (var i = 0; i < myArray.length-1; i++) {
        if (Math.abs(myArray[i] - myArray[i+1]) <= diff) {
            for (var j = i+1; j < myArray.length; j++) {
                var d = Math.abs(myArray[i] - myArray[j]);
                if (d < diff) {
                    diff = d;
                    result = Array(myArray[i], myArray[j]);
                } else if (d === diff) {
                    result.push(myArray[i], myArray[j]);
                }
            }
        }
    }
    console.log(result.join(' '))
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
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
