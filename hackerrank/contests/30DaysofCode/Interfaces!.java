// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-19-interfaces

class Calculator implements AdvancedArithmetic {
    public int divisorSum(int n) {
        int sum = n;
        for (int i = 1; i <= n/2; i++) {
            if (n % i == 0)
                sum += i;
        }
        return sum;
    }
}
