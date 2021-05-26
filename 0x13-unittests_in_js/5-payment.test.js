const sendPaymentRequestToApi = require('./5-payment');
const sinon = require('sinon');
const chai = require('chai');

describe('Suite 1', () => {
    let spy;
    let stub;

    beforeEach(() => {
        spy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        spy.restore();
        sinon.restore();
    });

    it('sendPaymentRequestToAPI w/ args (100, 20)', () =>{
        sendPaymentRequestToApi(100, 20);
        chai.expect(spy.calledWith('The total is: 120')).to.be.true;
        chai.expect(spy.calledOnce).to.be.true;
    });

    it('sendPaymentRequestToAPI w/ args (10, 10)', () =>{
        sendPaymentRequestToApi(10, 10);
        chai.expect(spy.calledWith('The total is: 20')).to.be.true;
        chai.expect(spy.calledOnce).to.be.true;
    });
});
