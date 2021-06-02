#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2);

/* slice two removes node and file path args[0] IS first arg */
/* if one exists */

if (typeof args[0] === 'undefined') {
  console.log('No argument');
} else {
  console.log(args[0]);
}
