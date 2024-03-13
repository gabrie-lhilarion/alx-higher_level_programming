#!/usr/bin/node

/**
 * Class:  Rectangle
 * Returns empty object if either h or w id <= 0
 */

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return this
    }
    this.width = w
    this.height = h
  }
}

module.exports = Rectangle
