function subStringFinder(str, subStr) {
  var len = str.length - subStr.length;

  // loop through string
  for (var i = 0; i <= len; i++) {
    if (str[i] == subStr[0]) {
      // loop through sub string
      for (var j = 1; j < subStr.length; j++) {
        if (subStr[j] == str[i+j]) {
          // if j is the last letter, we found a match
          if (j == subStr.length-1)
            return i;
        }
        else 
          break
      }
    }
  }
  return -1;
}
