const readFile = require('./2-read_file');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      try {
        resolve(readFile(path));
      } catch (error) {
        reject(error);
      }
    });
  });
}

module.exports = countStudents;
