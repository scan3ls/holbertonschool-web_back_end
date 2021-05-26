const calculateNumber = require('./0-calcul');
const assert = require('assert');

it('numbers containing fractions over 0.5 should round up', () => {
    assert.equal(calculateNumber(0.4, 0.4), 1);
});
it('numbers containing fractions under 0.5 should round down', () => {
    assert.equal(calculateNumber(0.2, 0.2), 0);
});
