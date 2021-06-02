#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2);

/* slice two removes node and file path args[0] IS first arg */
/* if one exists */

if (typeof args[0] === 'undefined' || isNaN(args[0])) {
  console.log('Missing size');
} else {
  let str = '';
  for (let i = 0; i < args[0]; i++) {
    str += 'X';
  }
  for (let i = 0; i < str.length; i++) {
    console.log(str);
  }
}
