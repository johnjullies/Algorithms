function mergeSortedArray(a, b) {
  	b.forEach(function(e) { 
  		a.push(e); 
  	});
  	return a.sort(function(a, b) {
  		return a - b;
  	});
}
