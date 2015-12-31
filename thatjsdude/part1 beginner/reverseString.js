function reverseString(str) {
  if (!str || str.length < 2) return str;
  
  return str.split('').reverse().join('');
}

// String extension: 

String.prototype.reverseString = function () {
  if(!this || this.length < 2) return this;
  
  return this.split('').reverse().join('');
}
