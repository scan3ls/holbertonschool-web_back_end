const getPaymentTokenFromApi = require('./6-payment_token');
const assert = require('assert');

describe('getPaymentTokenFromAPI', () => {
    it('Success', (done) => {
        const promise = getPaymentTokenFromApi(true);
        promise.then((data) => {
            assert.equal(data.data, 'Successful response from the API');
            done();
        });
    });
});
