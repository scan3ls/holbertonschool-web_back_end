export default function appendToEachArrayValue(array, appendString) {
    for (let str of array) {
      str = 1;
    }
    return array.map(x => appendString + x);
  }
