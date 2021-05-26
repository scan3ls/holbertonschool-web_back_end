const calculateNumber = require('./1-calcul');
const assert = require('assert');

describe('Calcultor functions', () => {
    it('Addition', () => { assert.equal(calculateNumber('SUM', 1.4, 4.5), 6) });
    it('Subraction', () => { assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4) });
    it('Division', () => { assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error') });
});
