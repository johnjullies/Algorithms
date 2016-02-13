// https://www.hackerrank.com/contests/7days-javascript/challenges/find-second-largest-number-in-an-array

function processData(myArray) {
    myArray.sort(function(a , b){ return b - a});
    for (var i = 1; i < myArray.length; i++) {
        if (myArray[i] != myArray[0]) {
            console.log(myArray[i]);
            break;
        }
    }
}


// tail starts here
process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input.split('\n')[1].split(' ').map(Number));
});
