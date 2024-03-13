#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return this
    }
    this.width = w
    this.height = h
  }

  print () {
    if (!this.width || !this.height) {
      console.log('')
      return
    }
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width))
    }
  }
}

module.exports = Rectangle
