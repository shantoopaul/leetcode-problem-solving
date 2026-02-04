/**
 * @param {string} s
 * @return {number}
 */
const scoreOfString = (str) => {
    let total = 0;
    for (let i = 0; i < str.length - 1; i++) {
        total += Math.abs(str.charCodeAt(i) - str.charCodeAt(i + 1));
    }
    return total;
};