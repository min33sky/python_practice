/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let profit = 0;
  let minValue = Number.MAX_VALUE;

  for (const price of prices) {
    minValue = Math.min(price, minValue);
    profit = Math.max(profit, price - minValue);
  }

  return profit;
};

console.log(maxProfit([7, 1, 5, 3, 6, 4]));
