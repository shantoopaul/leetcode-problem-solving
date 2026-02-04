/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
const addTwoPromises = async(promise1, promise2) => {
    [a, b] = await Promise.all([promise1, promise2]);
    return a + b;
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */