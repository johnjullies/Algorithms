// random between 5 to 7

function rand7() {
  function rand5(){
    return 1 + Math.random() * 4;
  }
  
  return 5 + rand5() / 5 * 2;
}
