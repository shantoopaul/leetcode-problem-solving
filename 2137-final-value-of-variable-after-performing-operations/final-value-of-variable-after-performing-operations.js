/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let x = 0;
    for (let op of operations) {
        op.includes('+') ? x++ : x--;
    }
    return x;
};