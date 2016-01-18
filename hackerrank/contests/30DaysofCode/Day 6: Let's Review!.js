// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-6-lets-review

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
    var n = parseInt(readLine());
    var spaces = n - 1;
    for (var i = 0; i < n; i++, spaces--) {
        console.log(Array(n).fill(' ').fill('#', spaces).join(''));
    }
}
