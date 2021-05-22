process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.resume();

process.stdin.on('readable', () => {
  const chunck = process.stdin.read();
  if (chunck !== null) {
    process.stdout.write(`Your name is: ${chunck}`);
  }
});

process.on('exit', () => {
  if (!process.stdin.isTTY) process.stdout.write('Closing\n');
});
