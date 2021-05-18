export default function cleanSet(set, startString) {
  const result = [];

  if (set instanceof Set === false) return '';
  if (typeof startString !== 'string') return '';
  if (startString.length <= 0) return '';

  [...set].forEach((value) => {
    if (typeof value !== 'string') return;
    if (value.startsWith(startString)) {
      result.push(value.substring(startString.length));
    }
  });

  return result.join('-');
}
