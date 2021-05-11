export default function gaurdrail(mathFunction) {
  const queue = [];
  const guard = 'Guardrail was processed';

  try {
    queue.push(mathFunction(), guard);
  } catch (error) {
    const errStr = `${error.name}: ${error.message}`;
    queue.push(errStr, guard);
  }

  return queue;
}
