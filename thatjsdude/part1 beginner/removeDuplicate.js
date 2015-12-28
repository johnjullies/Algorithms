function removeDuplicate(arr) {
  var exists = {},
      results = [], 
      elt;

  for (var i = 0; i < arr.length; i++) {
    elt = arr[i];
    if(!exists[elt]) {
      results.push(elt);
      exists[elt] = true;
    }
  }
  
  return results;
}
