#!/usr/bin/node

const args = process.argv.slice(2);

if (typeof args[0] === 'undefined' || isNaN(args[0])) {
  console.log('NaN');
} else if (typeof args[1] === 'undefined' || isNaN(args[1])) {
  console.log('NaN');
} else {
  console.log(adds(args[0], args[1]));
}

function adds (arg0, arg1) {
  return +arg0 + +arg1;
}
