#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch task data. Status code: ${response.statusCode}`);
    return;
  }

  const tasks = JSON.parse(body);
  const completedTasksByUser = {};

  tasks.forEach(task => {
    if (task.completed) {
      completedTasksByUser[task.userId] = (completedTasksByUser[task.userId] || 0) + 1;
    }
  });

  console.log(completedTasksByUser);
});
