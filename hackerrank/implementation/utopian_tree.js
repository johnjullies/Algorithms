function processData(input) {
    var parse_fun = function (s) { return parseInt(s, 10); };

    var lines = input.split('\n');
    var T = parse_fun(lines.shift());

    var data = lines.splice(0, T).map(parse_fun);

    // logic here
    for (var current = 0; current < T; current++) {
        if (data[current] < 1) {
            console.log(1);
        }   
        else {
            var height = 1;
            for (var i = 1; i <= data[current]; i++) {
                if (i % 2 == 0) height += 1;
                else height *= 2;
            }
            console.log(height);
        }
    }
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
var _input = "";
process.stdin.on("data", function (input) { _input += input; });
process.stdin.on("end", function () { processData(_input); });
