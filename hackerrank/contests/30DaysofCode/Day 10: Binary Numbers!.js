function processData(input) {
    var ar = input.split('\n').map(Number);
    for (var i = 1; i <= ar[0]; i++) {
        console.log(ar[i].toString(2));
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
