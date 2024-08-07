#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmEndPoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let character = [];
const names = [];

const requestCharacters = async () => {
  await new Promise(resolve => request(filmEndPoint, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      console.error('Error: ', err, '| StatusCode: ', res.statusCode);
    } else {
      const jsonBody = JSON.parse(body);
      character = jsonBody.characters;
      resolve();
    }
  }));
};

const requestNames = async () => {
  if (character.length > 0) {
    for (const p of character) {
      await new Promise(resolve => request(p, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          console.error('Error: ', err, '| StatusCode: ', res.statusCode);
        } else {
          const jsonBody = JSON.parse(body);
          names.push(jsonBody.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: Got no Characters for some reason');
  }
};

const getCharNames = async () => {
  await requestCharacters();
  await requestNames();

  for (const x of names) {
    if (x === names[names.length - 1]) {
      process.stdout.write(x);
    } else {
      process.stdout.write(x + '\n');
    }
  }
};

getCharNames();
