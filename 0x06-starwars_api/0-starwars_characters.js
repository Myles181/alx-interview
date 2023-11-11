#!/usr/bin/node

const axios = require('axios');

function getMovieCharacters(movieId) {
    // Star Wars API base URL
    const baseUrl = 'https://swapi.dev/api/';

    // Make a request to get information about the specified movie
    const filmUrl = `${baseUrl}films/${movieId}/`;

    axios.get(filmUrl)
        .then(response => {
            const filmData = response.data;

            // Extract characters from the film data
            const characters = filmData.characters || [];

            // Fetch and print the names of characters
            characters.forEach(characterUrl => {
                axios.get(characterUrl)
                    .then(characterResponse => {
                        const characterData = characterResponse.data;
                        console.log(characterData.name);
                    })
                    .catch(error => {
                        console.error(`Error fetching character data: ${error.message}`);
                    });
            });
        })
        .catch(error => {
            console.error(`Error fetching film data: ${error.message}`);
        });
}

if (process.argv.length !== 3) {
    console.log('Usage: node script.js <movie_id>');
    process.exit(1);
}

// Get the movie ID from the command line argument
const movieId = process.argv[2];

// Fetch and print characters for the specified movie
getMovieCharacters(movieId);

