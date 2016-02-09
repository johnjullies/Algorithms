// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-22-binary-search-trees

if (root == null)
  return 0;

var left = this.getHeight(root.left);
var right = this.getHeight(root.right);

return Math.max(left, right) + 1;
