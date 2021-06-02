#!/usr/bin/node

/* node and the path to your stcript will always be present - even if your program takes no arguments of its own, your script's interpreter and path are still considered arguments to the shell you're using. */

const process = require('process');

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('No argument found');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
