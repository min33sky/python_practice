/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  if (!s.toLowerCase().match(/\w+\b/g)) return true;
  let org = s
    .toLowerCase()
    .match(/[a-zA-Z0-9]+\b/g)
    .join('');
  let cmp = s
    .toLowerCase()
    .match(/[a-zA-Z0-9]+\b/g)
    .reverse()
    .map((v) => [...v].reverse().join(''))
    .join('');
  return org === cmp;
};
