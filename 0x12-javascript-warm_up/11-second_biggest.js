#!/usr/bin/node

const findSecondLargest = (...args) => {
    if (args.length <= 1) {
        console.log(0)
        return
    }

    const integers = args.map(Number).filter(Number.isInteger)

    const sortedIntegers = integers.sort((a, b) => b - a)

    if (sortedIntegers.length < 2) {
        console.log(0)
        return
    }

    console.log(sortedIntegers[1])
}

