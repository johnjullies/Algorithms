function isEven(n) {
  if (n > 1)
    return isEven(n - 2);
  return !Boolean(n);
}