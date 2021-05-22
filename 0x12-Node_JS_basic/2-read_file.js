const fs = require('fs');

function countStudents(path) {
  const invalidType = (arg) => typeof arg !== 'string' && typeof arg !== 'number' && !(arg instanceof URL) && !(arg instanceof Buffer);
  if (
    invalidType(path)
    || !(fs.existsSync(path))
  ) throw Error('Cannot load the database');

  const data = fs.readFileSync(path, 'utf8');

  const fields = {};
  const lineItems = data.split('\n');
  let numberOfStudents = 0;

  lineItems.forEach((value) => {
    const entry = value.split(',');
    if (entry.length !== 4) return;

    const field = entry[entry.length - 1];
    if (field === 'field') return;

    const firstName = entry[0];
    numberOfStudents += 1;

    if (!fields[field]) fields[field] = [];
    fields[field].push(firstName);
  });

  console.log(`Number of students: ${numberOfStudents}`);

  Object.keys(fields).forEach((key) => {
    if (key === '') return;
    const value = fields[key];
    console.log(`Number of students in ${key}: ${value.length}. List: ${value.join(', ')}`);
  });
}

module.exports = countStudents;
