export default function updateUniqueItems(map) {
  if (Object.getPrototypeOf(map) !== Object.getPrototypeOf(new Map())) throw Error('Cannot process');

  const update1To100 = (value, key) => {
    if (value === 1) map.set(key, 100);
  };

  map.forEach(update1To100);
}
