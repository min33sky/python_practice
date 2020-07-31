/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function (nums) {
  return nums
    .sort((a, b) => a - b)
    .reduce((p, c, i) => {
      return i % 2 === 0 ? p + c : p;
    }, 0);
};

console.log(arrayPairSum([1, 4, 2, 3]));
