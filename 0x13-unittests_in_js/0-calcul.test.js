const calculateNumber = require('./0-calcul');
const assert = require('assert');

describe('First Number rounded', () => {
    it('Round up', () => {
        assert.equal(calculateNumber(0.7, 0), 1);
    });
    it('Round Down', () => {
        assert.equal(calculateNumber(0.2, 0), 0);
    });

});

describe('Second Number rounded', () => {
    it('Round up', () => {
        assert.equal(calculateNumber(0, 0.7), 1);
    });
    it('Round down', () =>{
        assert.equal(calculateNumber(0, 0.2), 0);
    });
});

describe('Both Numbers Rounded', () => {
    it('Rounded UP', () =>{
        assert.equal(calculateNumber(0.5, 0.5), 2);
    });
    it('Rounded Down', () => {
        assert.equal(calculateNumber(0.2, 0.2), 0);
    });
});
