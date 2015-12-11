function countBs(string) {
  return countChar(string, "B");
}

function countChar(string, ch) {
  var count = 0;
  for (var i = 0; i < string.length; i++) {
    if (string.charAt(i) === ch)
      count++;
  }
  return count;
}