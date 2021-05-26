const assert = require('assert');
const request = require('request');
const url = 'http://127.0.0.1:7865'

describe('Index page', () => {
    it('Good Status', (done) => {
        request(url, (err, res, body) => {
            assert.equal(res.statusCode, 200);
            done();
        })
    });
    it('Correct output', (done) => {
        request(url, (err, res, body) => {
            assert.equal(body, 'Welcome to the payment system');
            done();
        });
    });
    it('No error response', (done) => {
        request(url, (err, res, body) => {
            assert.equal(err, null);
            done();
        });
    });
});

describe('Cart page', () => {
    it('Good status for valid cart id', (done) => {
        request(`${url}/cart/1`, (err, res, body) => {
            assert.equal(res.statusCode, 200);
            done();
        });
    });
    it('Correct output for valid cart id', (done) => {
        request(`${url}/cart/1`, (err, res, body) => {
            assert.equal(body, 'Payment methods for cart 1');
            done();
        });
    });
    it('No error for valid cart id', (done) => {
        request(`${url}/cart/1`, (err, res, body) => {
            assert.equal(err, null);
            done();
        });
    });
    it('Bad status for invalid cart id', (done) => {
        request(`${url}/cart/yes`, (err, res, body) => {
            assert.equal(res.statusCode, 404);
            done();
        });
    });
    it('Correct output for invalid cart id', (done) => {
        request(`${url}/cart/yes`, (err, res, body) => {
            assert.equal(body, 'Id must be a number');
            done();
        });
    });
    it('No error for invalid cart id', (done) => {
        request(`${url}/cart/yes`, (err, res, body) => {
            assert.equal(err, null);
            done();
        });
    });
});

describe('Available_Payments page', () => {
    it('Good status', (done) => {
        request(`${url}/available_payments`, (err, res, body) => {
            assert.equal(err, null);
            assert.equal(res.statusCode, 200);
            done();
        });
    });
    it('Correct Output', (done) => {
        request(`${url}/available_payments`, (err, res, body) => {
            assert.equal(err, null);
            assert.equal(body, '{"payment_methods":{"credit_cards":true,"paypal":false}}');
            done();
        });
    });
});

describe('Login page', () => {
    const validArgs = {
        url: `${url}/login`,
        method: 'POST',
        json: {'userName': 'jeff'}
    }
    const invalidArgs = {
        url: `${url}/login`,
        method: 'POST',
        json: {'xUserName': 'jeff'}
    }
    describe('Successful Login', () => {
        it('No Error', (done) => {
            request(validArgs, (err, res, body) => {
                assert.equal(err, null);
                done();
            })
        });
        it('Correct Status', (done) => {
            request.post(validArgs, (err, res, body) => {
                assert.equal(res.statusCode, 200);
                done();
            })
        });
        it('Correct Body', (done) => {
            request.post(validArgs, (err, res, body) => {
                assert.equal(body, "Welcome jeff");
                done();
            })
        });
    });
    describe('Failed Login', () => {
        it('No Error', (done) => {
            request.post(invalidArgs, (err, res, body) => {
                assert.equal(err, null);
                done();
            })
        });
        it('Correct Status', (done) => {
            request.post(invalidArgs, (err, res, body) => {
                assert.equal(res.statusCode, 404);
                done();
            })
        });
        it('Correct Body', (done) => {
            request.post(invalidArgs, (err, res, body) => {
                assert.equal(body, "Unknown user");
                done();
            })
        });
    });
});
