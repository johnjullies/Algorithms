// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-3-if-statements

process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function main() {
    var N = parseInt(readLine());
    
    if (N%2 > 0)
        console.log("Weird");
    else {
        if (N>=2 && N<=5)
            console.log("Not Weird");
        else if (N>=6 && N<=20)
            console.log("Weird");
        else if (N > 20)
            console.log("Not Weird");
    }
}
