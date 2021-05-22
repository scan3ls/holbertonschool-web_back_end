const readFile = require('./2-read_file');

function countStudents(path) {
  return new Promise((resolve) => {
    setTimeout(() => {
      readFile(path);
      resolve();
    });
  });
}

module.exports = countStudents;
