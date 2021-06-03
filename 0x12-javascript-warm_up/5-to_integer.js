!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2);

/* slice two removes node and file path args[0] IS first arg */
/* if one exists */

if (typeof args[0] === 'undefined' || isNaN(args[0])) {
  console.log('Not a number');
} else {
  console.log('My number: %i', args[0]);
}
