/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicateLetters = function (s) {
  let stack = []; // 문자를 담을 스택
  let seen = new Set(); // 중복을 검사하기위한 SET
  let counter = {}; // 문자 별 개수를 저장할 객체

  // 문자열에서 각 문자들의 개수를 저장한다.
  for (const char of s) {
    counter[char] ? (counter[char] += 1) : (counter[char] = 1);
  }

  for (let i = 0; i < s.length; i++) {
    counter[s[i]] -= 1; // 해당 문자를 확인했으니 개수 업데이트
    if (seen.has(s[i])) continue; // 이미 처리한 문자는 스킵

    /*
     * 현재 문자가 스택의 가장 마지막 문자보다 사전 순이 앞서며
     * 그 문자가 문자열에 1개 이상 남아있을경우 삭제하고 그 자리에 현재 문자를 넣는다.
     */
    while (
      stack.length > 0 &&
      s[i] < stack[stack.length - 1] &&
      counter[stack[stack.length - 1]] > 0
    ) {
      seen.delete(stack.pop()); // 해당 문자가 삭제되었으니 SET에서도 삭제하자
    }

    // 해당 문자를 스택에 넣고 중복 체크를 위한 SET에도 넣는다.
    stack.push(s[i]);
    seen.add(s[i]);
  }

  return stack.join('');
};

removeDuplicateLetters('cbacdcbc');
