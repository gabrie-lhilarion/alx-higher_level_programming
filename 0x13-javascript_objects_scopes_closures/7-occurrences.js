#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurances = 0
  list.forEach(element => {
    if (element === searchElement) occurances += 1
  })

 return occurances
}


