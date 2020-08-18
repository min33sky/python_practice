/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicateLetters = function (s) {
  let stack = [];
  let seen = new Set();
  let counter = {};

  // 문자의 개수를 저장
  for (const char of s) {
    counter[char] ? (counter[char] += 1) : (counter[char] = 1);
  }

  for (let i = 0; i < s.length; i++) {
    counter[s[i]] -= 1;
    // 이미 처리한 문자는 스킵
    if (seen.has(s[i])) continue;

    // 현재 문자가 가장 마지막 문자보다 사전 순이 앞서며 가장 최근 문자가 1개 이상 남아있을경우
    while (
      stack.length > 0 &&
      s[i] < stack[stack.length - 1] &&
      counter[stack[stack.length - 1]] > 0
    ) {
      seen.delete(stack.pop());
    }

    stack.push(s[i]);
    seen.add(s[i]);
  }

  return stack.join('');
};

removeDuplicateLetters('cbacdcbc');
