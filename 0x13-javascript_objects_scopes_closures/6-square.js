#!/usr/bin/node

const MySquare = require('./5-square')

class Square extends MySquare {
  constructor(size) {
    super(size, size)
  }
  
charPrint(c) {
  if (!c) {
    c = 'X'
  }

  let row = c.repeat(this.width)
  for (let i = 0; i < this.height; i++) {
    console.log(row)
  }
  }
}

module.exports = Square
