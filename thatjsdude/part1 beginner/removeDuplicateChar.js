function removeDuplicateChar(str) {
  var charCount = {}, 
      newStr = [];

  for (var i = 0; i < str.length; i++) {
    var char = str[i];
    if (charCount[char]) 
      charCount[char]++;
    else
      charCount[char] = 1;
  }

  for (var i in charCount) {
    if (charCount[i]==1)
      newStr.push(i);
  }

  return newStr.join('');
}
