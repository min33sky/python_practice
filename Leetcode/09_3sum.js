/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  let results = [];
  let sorted = nums.sort((a, b) => a - b); // 정렬

  // 좌측, 우측 포인터를 제외 한 개수만큼 순회
  for (let i = 0; i < sorted.length - 2; i++) {
    // 현재 인덱스의 값이 이전과 동일할 경우 패스한다.
    if (i > 0 && sorted[i] === sorted[i - 1]) {
      continue;
    }

    let left = i + 1;
    let right = sorted.length - 1;
    let sum = 0;

    // 투 포인터들을 움직여서 세 수의 합을 구한다.
    while (left < right) {
      sum = sorted[i] + sorted[left] + sorted[right];
      if (sum < 0) {
        left++;
      } else if (sum > 0) {
        right--;
      } else {
        // 결과 배열에 추가
        results.push([sorted[i], sorted[left], sorted[right]]);

        // 중복 값은 순회 패스
        while (left < right && sorted[left] === sorted[left + 1]) {
          left++;
        }
        while (left < right && sorted[right] === sorted[right - 1]) {
          right++;
        }

        // 투 포인터 이동
        left++;
        right--;
      }
    }
  }

  return results;
};

console.log(threeSum([-1, 0, 1, 2, -1, -4]));
