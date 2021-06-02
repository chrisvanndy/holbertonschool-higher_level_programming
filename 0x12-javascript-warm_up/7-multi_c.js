#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2);

/* slice two removes node and file path args[0] IS first arg */
/* if one exists */

if (typeof args[0] === 'undefined' || isNaN(args[0])) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < args[0]; i++) {
    console.log('C is fun');
  }
}
