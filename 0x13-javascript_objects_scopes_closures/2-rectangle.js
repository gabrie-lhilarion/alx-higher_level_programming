#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    this.width = w
    this.height = h
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {}
    }
  }
}

module.exports = Rectangle
