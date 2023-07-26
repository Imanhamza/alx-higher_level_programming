#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
      const todosData = JSON.parse(body);
	// console.log(todosData);
      const completedTasks = {};
      
      for (let i = 0; i < todosData.length; i++) {
        const todo = todosData[i];
	// console.log(todo.title);
	if (todo.completed) {
	  if (completedTasks[todo.userId]) {
	    completedTasks[todo.userId]++;
	  } else {
	      completedTasks[todo.userId] = 1;
	}
	}
	}
	console.log(completedTasks);
}
}
);
