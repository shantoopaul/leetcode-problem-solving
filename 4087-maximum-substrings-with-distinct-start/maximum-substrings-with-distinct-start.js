/**
 * @param {string} s
 * @return {number}
 */
var maxDistinct = function(s) {
    let chArr=[];
    let res = 0;
    chArr.length=26;
    chArr.fill(0);

    for(let i = 0; i < s.length; i++) chArr[s.charCodeAt(i) - 97]++;

    for(let i=0;i<26;i++) if(chArr[i]) res++;
    return res;
    // return new Set(s).size
};