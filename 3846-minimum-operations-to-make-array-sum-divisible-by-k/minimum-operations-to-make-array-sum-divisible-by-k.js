/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums, k) {
    total = nums.reduce((a, b) => a + b, 0);
    return total % k;
};