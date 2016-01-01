// reverse words in a sentence:

function reverseWords(str) {
  return str.split(' ').reverse();
}

// words are in place but reverse:

function reverseInPlace(str) {
  return str.split(' ').reverse().join(' ').split('').reverse().join('');
}

// > reverseInPlace('I am the good boy');
// = "I ma eht doog yob"
