/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let stack = [];
  // 닫는 괄호를 검색하기 위한 해시 태이블
  let table = {
    ')': '(',
    '}': '{',
    ']': '[',
  };

  for (const char of s) {
    // 여는 괄호일 경우 스택에 푸시
    if (!table[char]) {
      stack.push(char);
      // 닫는 괄호일 경우 스택이 비어있거나 팦한 괄호와 같지 않을 경우 false
    } else if (stack.length === 0 || stack.pop() !== table[char]) {
      return false;
    }
  }

  // 스택이 비어있어야 유효
  return stack.length === 0;
};

console.log(isValid('()'));
