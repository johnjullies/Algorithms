// swap two numbers without temporary variable

function swapNum(a, b) {
  console.log('before swap: ', 'a: ', a, 'b: ', b);
  b = b - a;
  a = a + b;
  b = a - b;
  console.log('after swap: ', 'a: ', a, 'b: ', b);  
}
