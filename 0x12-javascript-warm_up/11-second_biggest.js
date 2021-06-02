#!/usr/bin/node

const args = process.argv.slice(2);

if (args[0] === 'undefined' || args.length === 1) {
  console.log('%i', 0);
} else {
  console.log(secondMax(args));
}

function secondMax (arg) {
  const max = Math.max.apply(null, args);
  args.splice(args.indexOf(max), 1);
  return Math.max.apply(null, args);
}
