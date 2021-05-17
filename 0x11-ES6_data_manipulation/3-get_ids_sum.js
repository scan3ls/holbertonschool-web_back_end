import getListStudentIds from './1-get_list_student_ids';

export default function getStudentIdsSum(students) {
  const sum = (prev, curr) => prev + curr;

  return getListStudentIds(students).reduce(sum);
}
