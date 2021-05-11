export default function gaurdrail(mathFunction){
    let queue = [];
    const guard = 'Guardrail was processed';

    try {
        queue.push(mathFunction(), guard);
    } catch (error) {
        const err_str = `${error.name}: ${error.message}`
        queue.push(err_str, guard);
    }

    return queue;
}
