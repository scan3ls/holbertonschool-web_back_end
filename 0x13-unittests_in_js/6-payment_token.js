function getPaymentTokenFromAPi(success) {
    if (success === true) {
        return new Promise((resolve, reject) => {
            try {
                resolve({data: 'Successful response from the API' });
            } catch (err) {
                reject(err);
            }
        });
    }
}

module.exports = getPaymentTokenFromAPi;
