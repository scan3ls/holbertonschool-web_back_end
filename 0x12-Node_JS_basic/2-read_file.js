const fs = require('fs');

function countStudents(path) {
  if (
    typeof path !== 'string'
        && typeof path !== 'number'
        && !(path instanceof URL)
        && !(path instanceof Buffer)
  ) return;

  try {
    const data = fs.readFileSync(path, 'utf-8');

    const fields = {};
    const split = data.split('\n');
    let numberOfStudents = 0;

    split.forEach((value) => {
      const entry = value.split(',');
      if (entry.length < 4) return;

      const field = entry[entry.length - 1];
      if (field === 'field') return;

      const firstName = entry[0];
      numberOfStudents += 1;

      if (!fields[field]) fields[field] = [];
      fields[field].push(firstName);
    });

    console.log('Number of students: ', numberOfStudents);

    Object.keys(fields).forEach((key) => {
      if (key === '') return;
      const value = fields[key];
      console.log(`Number of students in ${key}: ${value.length}. List: ${value.join(', ')}`);
    });
  } catch (error) {
    throw Error('Cannot load the database');
  }
}

module.exports = countStudents;
