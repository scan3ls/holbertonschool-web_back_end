function calculateNumber(type, a, b) {
    switch (type) {
        case 'SUM':
            return Math.round(a + b);
        case 'SUBTRACT':
            return Math.round(a) - Math.round(b);
        case 'DIVIDE':
            if (Math.round(b) === 0) return 'Error';
            return (Math.round(a) / Math.round(b));
        default:
            throw Error('Invalid type for function');
    }
}

module.exports = calculateNumber;
