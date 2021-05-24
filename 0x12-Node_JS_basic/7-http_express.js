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

  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  res.write('This is the list of our students\n');
  promise
    .then((data) => {
      const { fields } = data;
      const { studentCount } = data;

      res.write(`Number of students: ${studentCount}`);
      Object.keys(fields).forEach((key) => {
        if (key === '') return;
        const value = fields[key];
        res.write(`\nNumber of students in ${key}: ${value.length}. List: ${value.join(', ')}`);
      });
    })
    .catch((err) => {
      res.write(err.message);
    })
    .finally(() => {
      res.end();
    });
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});

module.exports = app;
