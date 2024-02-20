#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    process.exit(1);
  }

  // check response status code
  if (response.statusCode !== 200) {
    process.exit(1);
  }

  try {
    // parse data
    const todos = JSON.parse(body);

    const completedTasksByUser = {};

    todos.forEach(todo => {
      if (todo.completed) {
        completedTasksByUser[todo.userId] = (completedTasksByUser[todo.userId] || 0) + 1;
      }
    });
    console.log(completedTasksByUser);
  } catch (err) {
    process.exit(1);
  }
});
