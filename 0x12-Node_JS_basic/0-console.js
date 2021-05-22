function displayMessage(msg) {
  if (typeof msg !== 'string') return;
  process.stdout.write(`${msg}\n`);
}

module.exports = displayMessage;
