// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-14-scope-and-imports

public Difference(int[] a) {
  elements = a;
}

public void computeDifference() {
  int max = 0;
  for (int i = 0; i < elements.length-1; i++) {
      for (int j = i+1; j < elements.length; j++) {
          int diff = Math.abs(elements[i] - elements[j]);
          if (diff > max) 
              max = diff;
      }
  }
  maximumDifference = max;
}
