#!/usr/bin/node

exports.logMe = (function () {
  let count = 0; // Variable enclosed in a closure

  return function (item) {
    console.log(`${count}: ${item}`);

    count++;
  };
})();

  