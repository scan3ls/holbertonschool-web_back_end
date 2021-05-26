const calculateNumber = require('./2-calcul_chai');
const chai = require('chai');
const expect = chai.expect;

describe('Calcultor functions', () => {
    it('Addition', () => { 
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('Subraction', () => { 
        expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('Division', () => {
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
});
