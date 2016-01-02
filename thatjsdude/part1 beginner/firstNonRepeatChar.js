function firstNonRepeatChar(str) {
  var charCount = {};

  for (var i = 0; i < str.length; i++) {
    var char = str[i];
    if (charCount[char])
      charCount[char]++;
    else
      charCount[char] = 1;
  }

  for (var j in charCount) {
    if (charCount[j]==1)
      return j;
  }
}  

// > firstNonRepeatChar('the quick brown fox jumps then quickly blow air');
// = "f"
