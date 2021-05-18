export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer);

  if (position <= 0 >= length) {
    throw Error('Position outside range');
  }
  view.setUint8(position, value);

  return view;
}
