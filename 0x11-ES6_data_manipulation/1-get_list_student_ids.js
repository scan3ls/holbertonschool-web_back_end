export default function getListStudentIds(array) {
  if (Array.isArray(array) === false) {
    return [];
  }

  const getIds = (student) => student.id;

  return array.map(getIds);
}
