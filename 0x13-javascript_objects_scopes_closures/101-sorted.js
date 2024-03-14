#!/usr/bin/node

const { dict } = require('./101-data')

const invertDictionary = (originalDict) => {
    const invertedDict = {}

    for (const userId in originalDict) {
        const occurrences = originalDict[userId]

        if (invertedDict[occurrences]) {
            invertedDict[occurrences].push(userId)
        } else {
            invertedDict[occurrences] = [userId]
        }
    }

    return invertedDict
};

const invertedDict = invertDictionary(dict)

console.log(invertedDict)

