/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  /**
   *  정렬 한 문장을 해쉬테이블의 키로 사용하고
   *  원본 문장을 배열에 추가
   *
   */
  const result = strs.reduce((p, c) => {
    let sortedWord = c.split('').sort().join('');
    if (p[sortedWord]) {
      p[sortedWord].push(c);
    } else {
      p[sortedWord] = [c];
    }
    return p;
  }, {});

  return Object.keys(result).map((v) => [...result[v]]);
};

console.log(groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']));
