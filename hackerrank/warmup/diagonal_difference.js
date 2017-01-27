function processData(input) {
    //Enter your code here
    var _inputArray = input.split("\n");
    var n = parseInt(_inputArray[0], 10);
    var matrix = [];
    for (var i = 0; i < n; i++) {
        matrix[i] = _inputArray[i + 1].split(" ").map(Number);
    }
    
    var s1 = 0;
    var s2 = 0;
    var j = n - 1;
    for (var i = 0; i < n; i++) {
        s1 += matrix[i][i];
        s2 += matrix[i][j];
        j--;
    }
    console.log(Math.abs(s1 - s2));
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
