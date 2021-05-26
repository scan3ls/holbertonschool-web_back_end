const calculateNumber = require('./2-calcul_chai');
const chai = require('chai');
const expect = chai.expect;

describe('DIVISION', () => {
    it('Divide by Zero', () => { expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error') });
    it('Valid Division', () => { expect(calculateNumber('DIVIDE', 4, 2)).to.equal(2) });
});

describe('ADDITION', () => {
    it('Valid Addition', () => { expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6) });
});

describe('SUBTRACTION', () => {
    it('Valid subtraction', () => { expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4) });
});
