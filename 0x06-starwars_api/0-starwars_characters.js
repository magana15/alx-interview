#!/usr/bin/node

// Importing the 'request' library
const request = require('request');

// Define constant with the base URL of the Star Wars API
const API_URL = 'https://swapi-api.alx-tools.com/api';

// Checks if number of command line arguments is > 2
if (process.argv.length > 2) {
  // Makes a request to the film resource for the specified film ID.
  
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    // If an error occurred during the request, logs the error
    if (err) {
      console.log(err);
    }
    // Get the characters URL from the film's response body.
    const charactersURL = JSON.parse(body).characters;

    // Creates an array of Promises that resolve with the
    //names of the characters
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        // Make a request to the character resource
        request(url, (promiseErr, __, charactersReqBody) => {
          // If an error occurs during the request, rejects
          //the Promise with the error
          if (promiseErr) {
            reject(promiseErr);
          }
          // Resolves the Promise with the name of the character
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    // Waits for all Promises to resolve and log the names
    //of the characters, separated by new lines.
    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
