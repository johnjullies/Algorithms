var size = 8;

var board = "";

for (var row = 0; row < size; row++) {
  for (var col = 0; col < size; col++) {
    if ((col + row) % 2 == 0)
      board += " ";
    else
      board += "#";
  }
  board += "\n";
}

console.log(board);