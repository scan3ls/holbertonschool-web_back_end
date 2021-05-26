const calculateNumber = require('./0-calcul');
const assert = require('assert');

it('First Number rounded', () => {
    assert.equal(calculateNumber(0.7, 0), 1);
});
it('Second Number rounded', () => {
    assert.equal(calculateNumber(0, 0.7), 1);
});
it('Both Numbers Rounded', () =>{
    assert.equal(calculateNumber(0.5, 0.5), 2);
});
