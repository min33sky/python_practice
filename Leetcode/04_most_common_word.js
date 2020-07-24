/**
 * @param {string} paragraph
 * @param {string[]} banned
 * @return {string}
 */
var mostCommonWord = function (paragraph, banned) {
  let dict = {};
  let filterParagraph = paragraph
    .toLowerCase()
    .match(/[a-zA-Z]+/g)
    .filter((v) => !banned.includes(v));

  filterParagraph.forEach((v) => {
    if (!dict[v]) {
      dict[v] = 1;
    } else {
      dict[v] += 1;
    }
  });

  return Object.keys(dict).reduce((p, c) => (dict[p] > dict[c] ? p : c));
};

console.log(
  mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', [
    'hit',
  ]),
);
