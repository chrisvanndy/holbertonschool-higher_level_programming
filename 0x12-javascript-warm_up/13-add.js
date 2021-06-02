#!/usr/bin/node

/* "//<somefile>" exports a function to app that calls it */

// 13-add.js
exports.add = function (a, b) {
  return (a + b);
};
