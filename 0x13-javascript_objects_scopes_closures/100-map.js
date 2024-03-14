#!/usr/bin/node

const { list } = require('./100-data');


console.log('Initial list:', list);

const newList = list.map((value, index) => value * index);

console.log('New list:', newList);
