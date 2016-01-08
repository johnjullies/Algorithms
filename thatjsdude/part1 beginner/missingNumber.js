function missingNumber(arr){
  var n = arr.length + 1, 
      sum = 0,
      expectedSum = n * (n+1)/2;
  
  sum = arr.reduce(function(a, b) { return a + b; });
  
  return expectedSum - sum;
}

// missingNumber([5, 2, 6, 1, 3]);
// > 4
