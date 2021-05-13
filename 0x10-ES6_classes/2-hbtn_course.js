export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name === 'string') this._name = name;
    if (typeof length === 'number') this._length = length;
    if (typeof students === 'object') {
      if (typeof students[0] === 'string') this._students = students;
    }
  }

  get name() { return this._name; }

  set name(value) {
    if (typeof value !== 'string') throw TypeError('Name must be a string');
    this._name = value;
  }

  get length() { return this._length; }

  set length(value) {
    if (typeof value !== 'number') throw TypeError('Length must be a number');
    this._length = value;
  }

  get students() { return this._students; }

  set students(value) {
    if (typeof value !== 'object') throw TypeError('Students must be a list of strings');
    if (typeof value[0] !== 'string') throw TypeError('Students must be a list of strings');
    this._students = value;
  }
}
