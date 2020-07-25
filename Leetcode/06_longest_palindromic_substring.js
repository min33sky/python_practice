/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  if (s.length < 2 || s === [...s].reverse().join('')) {
    return s;
  }

  let result = '';

  for (const i in s) {
    let str1 = expand(s, Number(i), Number(i) + 1);
    let str2 = expand(s, Number(i), Number(i) + 2);
    // 가장 긴 팰린드롬 문자열을 찾아서 리턴한다.
    result = [result, str1, str2].sort((a, b) => b.length - a.length)[0];
  }

  return result;
};

function expand(str, left, right) {
  while (left >= 0 && right < str.length && str[left] === str[right]) {
    left--;
    right++;
  }
  return str.slice(left + 1, right);
}

console.log(longestPalindrome('babad'));
console.log(longestPalindrome('cbbd'));
console.log(longestPalindrome('a'));
console.log(longestPalindrome('aba'));
