#!/usr/bin/node

const fs = require('fs')

const concatFiles = (File1, File2, destinationFile) => {
  fs.readFile(File1, 'utf8', (err, data1) => {
    if (err) {
      console.error(`Error reading file ${File1}: ${err}`)
      return
    }

    fs.readFile(File2, 'utf8', (err, data2) => {
      if (err) {
        console.error(`Error reading file ${File2}: ${err}`)
        return
      }

      const concatenatedData = data1 + data2

      fs.writeFile(destinationFile, concatenatedData, (err) => {
        if (err) {
          console.error(`Error writing to file ${destinationFile}: ${err}`)
        }
      })
    })
  })
}

// Usage: node concatFiles.js sourceFile1.txt sourceFile2.txt destinationFile.txt
const [,, sourceFile1, sourceFile2, destinationFile] = process.argv
concatFiles(sourceFile1, sourceFile2, destinationFile)
