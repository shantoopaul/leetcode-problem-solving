/**
 * @param {string} s
 * @return {number}
 */
var maxDistinct = function(s) {
    // let res = new Set();
    // for (let x of s) {
    //     res.add(x)
    // }
    // return res.size;
    return new Set(s).size
};