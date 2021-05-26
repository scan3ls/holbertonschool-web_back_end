const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');
const chai = require('chai');
const sinon = require('sinon');

describe('Spying', () => {
    it('Function called', () => {
        const spy = sinon.spy(Utils, 'calculateNumber');
        sendPaymentRequestToApi(100, 20);

        chai.expect(spy.calledWith('SUM', 100, 20)).to.be.true;
        spy.restore();
    });
});