// Time: O(n)

function fibonacci(n) {
	var fibo = [0, 1];

	if (n <= 2) 
		return 1;

	for (var i = 2; i <= n; i++) {
		fibo[i] = fibo[i-1] + fibo[i-2];
	}

	return fibo[n];
}

// recursive alternative:
// Time: O(2^n)

function fibo(n) {
	if (n <= 1) 
		return n;
	else 
		return fibo(n-1) + fibo(n-2);
}
