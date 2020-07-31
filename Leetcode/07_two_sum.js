/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  // 검색을 위해서 배열을 해쉬테이블로 변환
  const hash = {};
  for (let i = 0; i < nums.length; i++) {
    // 해쉬 테이블에 target - nums[i] 값이 존재 할 때 종료
    if (hash[target - nums[i]] !== undefined) {
      return [hash[target - nums[i]], i];
    }
    // 해쉬 테이블에 추가
    hash[nums[i]] = i;
  }
  return [];
};

console.log(twoSum([2, 7, 11, 15], 9));
console.log(twoSum([2, 5, 5, 11], 10));
console.log(twoSum([3, 2, 4], 6));
