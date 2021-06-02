#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2);

/* slice two removes node and file path args[0] IS first arg */
/* if one exists */

console.log('%s is %s', args[0], args[1]);
