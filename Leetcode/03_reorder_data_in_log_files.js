/**
 * @param {string[]} logs
 * @return {string[]}
 */
var reorderLogFiles = function (logs) {
  console.log(
    logs
      .filter((log) => /[a-z]$/.test(log))
      .sort((a, b) =>
        a
          .replace(/^(\S+)\s(.*)/, '$2$1')
          .localeCompare(b.replace(/^(\S+)\s(.*)/, '$2$1')),
      )
      .concat(logs.filter((log) => /\d$/.test(log))),
  );
};

console.log(
  reorderLogFiles([
    'dig1 8 1 5 1',
    'let1 art can',
    'dig2 3 6',
    'let2 own kit dig',
    'let3 art zero',
  ]),
);
