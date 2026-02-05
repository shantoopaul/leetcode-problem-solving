/**
 * @param {number[]} nums
 * @return {number[]}
 */
var buildArray = function(nums) {
    let ans = [];
    for (let i in nums) ans.push(nums[nums[i]])
    return ans;
};