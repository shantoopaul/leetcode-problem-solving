/**
 * @param {number[]} nums
 * @return {number[]}
 */
const getConcatenation = (nums) => {
    const x = [...nums];
    return [...nums, ...x]
};