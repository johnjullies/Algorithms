// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-20-review-plus-more-string-methods

function processData(input) {
    var newstr = input.replace(/[\!\[\,\?\.\\\_\'\@\+\]]/g, ' ').trim();
    newstr = newstr.replace(/\s+/g, ' ').trim();
    var inputarray = [];
    if (newstr.length > 0)
        inputarray = newstr.split(' ');
    
    console.log(inputarray.length);
    inputarray.forEach(function(word){ console.log(word); });
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
