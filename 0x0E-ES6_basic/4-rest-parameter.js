import { count } from 'console';

export default function returnHowManyArguments(...Argv) {
  return Argv.slice().length;
}
