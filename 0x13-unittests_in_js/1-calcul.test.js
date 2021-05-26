const calculateNumber = require('./1-calcul');
const assert = require('assert');



describe('DIVISION', () => {
    it('Divide by Zero', () => { assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error') });
    it('Valid Division', () => { assert.equal(calculateNumber('DIVIDE', 4, 2), 2) });
});

describe('ADDITION', () => {
    it('Valid Addition', () => { assert.equal(calculateNumber('SUM', 1.4, 4.5), 6) });
});

describe('SUBTRACTION', () => {
    it('Valid subtraction', () => { assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4) });
});
