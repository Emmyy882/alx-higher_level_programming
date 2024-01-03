#!/usr/bin/node

const request = require('request');

request
  .get(process.argv[2])
  .on('reponse', response => {
    console.log(`code: ${response.statusCode}`);
  });
