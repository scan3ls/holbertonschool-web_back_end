const express = require('express');
const readFile = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const database = process.argv[2];
  const promise = readFile(database);

  promise
  .then( (data) => {
    const { fields } = data;
    const { studentCount } = data;

    let output = `This is the list of our students\nNumber of students: ${studentCount}`;

    Object.keys(fields).forEach((key) => {
      if (key === '') return;
      const value = fields[key];
      output = output + (`\nNumber of students in ${key}: ${value.length}. List: ${value.join(', ')}`);
    });
    res.send(output);
  })
  .catch(err => {
    let output = `This is the list of our students\n${err.message}`
    res.send(ouput);
  })
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});

module.exports = app;
