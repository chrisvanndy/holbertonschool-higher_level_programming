#!/usr/bin/node

const args = process.argv.slice(2);

if (args[0] === 'undefined' || isNaN(args[0]) || args[0] === 0) {
  console.log('%i', 1);
} else {
  console.log(fact(args[0]));
}

function fact (x) {
  return (x !== 1) ? x * fact(x - 1) : 1;
}
