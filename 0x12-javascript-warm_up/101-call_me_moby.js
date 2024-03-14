#!/usr/bin/node

const callXTimes = (x, theFunction) => {
    for (let i = 0; i < x; i++) {
        theFunction()
    }
}

module.exports = { callXTimes }
