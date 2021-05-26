const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');
const chai = require('chai');
const sinon = require('sinon');

describe('Spying', () => {
    it('Function called', () => {
        const stub = sinon.stub(Utils, 'calculateNumber');
        stub.returns(10);

        const spy = sinon.spy(console, 'log');
        const result = sendPaymentRequestToApi(100, 20);

        chai.expect(stub.calledWith('SUM', 100, 20)).to.be.true;
        chai.expect(spy.calledWith('The total is: 10')).to.be.true;

        stub.restore();
    });
});
