#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = []
  list.forEach(element => {
    reversed.unshift(element)
  });

  return reversed
}
