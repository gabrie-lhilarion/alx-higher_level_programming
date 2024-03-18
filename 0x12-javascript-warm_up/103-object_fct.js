#!/usr/bin/node

const myObject = {
    type: 'object',
    value: 12
};

const incr = () => {
    if (!isNaN(myObject.value)) {
        myObject.value++;
    }
};

incr();
console.log(myObject);
