#!/usr/bin/node

const factorial = (n) => {

    if (n === 0 || isNaN(n)) {
        return 1
    }

    return n * factorial(n - 1)
}


