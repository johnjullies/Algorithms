// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-8-dictionaries-and-maps

function processData(input) {
    var ar = input.split('\n');
    var idx = 0;
    var n = Number(ar[idx++]);
    var phonebook = Object.create(null);
    
    for (var i = 0; i < n; i++) {
        phonebook[ar[idx++]] = ar[idx++];
    }
    
    while (idx < ar.length) {
        var query = ar[idx++];
        if (phonebook[query])
            console.log(query+"="+phonebook[query]);
        else
            console.log("Not found");
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
