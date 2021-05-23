const http = require('http');
const readFile = require('./3-read_file_async');
// const { runInNewContext } = require('vm');

const host = '127.0.0.1';
const port = 1245;

const index = (res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello Holberton School!');
};

const students = (res, url = process.argv[2]) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  const promise = readFile(url);

  promise
    .then((data) => {
      const { fields } = data;
      const { studentCount } = data;

      res.write('This is the list of our students\n');
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
};

const app = http.createServer((req, res) => {
  const endpoint = {
    '/': index,
    '/students': students,
  };

  endpoint[req.url](res);
});

app.listen(port, host);

module.exports = app;
