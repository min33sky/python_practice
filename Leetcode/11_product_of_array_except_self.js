/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  let result = [];
  let p = 1; // 곱셈을 위한 변수
  // * 1. 해당 인덱스의 왼쪽 값들을 전부 곱하자
  for (let i = 0; i < nums.length; i++) {
    result.push(p);
    p = p * nums[i];
  }

  // * 2. 오른족 값들의 곱을 곱한다.

  p = 1; // 다시 곱셈을 위해서 초기화

  for (let i = result.length - 1; i >= 0; i--) {
    result[i] = result[i] * p;
    p = p * nums[i];
  }

  return result;
};

console.log(productExceptSelf([1, 2, 3, 4]));
