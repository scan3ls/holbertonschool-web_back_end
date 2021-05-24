import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    const database = process.argv[2];
    const promise = readDatabase(database);

    response.set('Content-Type', 'text/plain');
    response.status(200);
    response.write('This is the list of our students');
    promise
      .then((data) => {
        const { fields } = data;
        const { studentCount } = data;

        response.write(`Number of students: ${studentCount}`);
        Object.keys(fields).forEach((key) => {
          if (key === '') return;
          const value = fields[key];
          response.write(`\nNumber of students in ${key}: ${value.length}. List: ${value.join(', ')}`);
        });
      })
      .catch((err) => {
        response.status(500);
        response.write(err.message);
      })
      .finally(() => {
        response.end();
      });
  }

  static getAllSudentsByMajor(request, response) {
    const database = process.argv[2];
    const promise = readDatabase(database);

    response.set('Content-Type', 'text/plain');
    response.status(200);

    promise
      .then((data) => {
        const { major } = request.params;
        switch (major) {
          case 'CS':
            response.send(`List: ${data.fields.CS.join(', ')}`);
            break;
          case 'SWE':
            response.send(`List: ${data.fields.SWE.join(', ')}`);
            break;
          default:
            response.status(500);
            response.send('Major parameter must be CS or SWE');
            break;
        }
      })
      .catch((err) => {
        response.status(500);
        response.send(err.message);
      });
  }
}

module.exports = StudentsController;
