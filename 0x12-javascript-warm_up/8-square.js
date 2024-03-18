#!/usr/bin/node

const size = parseInt(process.argv[2])

// Check if size is a valid integer
if (isNaN(size)) {
    console.log("Missing size")
} else {

    for (let i = 0; i < size; i++) {
        let line = ""
        for (let j = 0; j < size; j++) {
            line += "X"
        }
        console.log(line)
    }
}
