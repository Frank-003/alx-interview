#!/usr/bin/node

const https = require('https');

// Function to fetch JSON data from a URL
const fetchData = (url) => {
    return new Promise((resolve, reject) => {
        https.get(url, (res) => {
            let data = '';

            res.on('data', (chunk) => {
                data += chunk;
            });

            res.on('end', () => {
                try {
                    resolve(JSON.parse(data));
                } catch (error) {
                    reject(`Error parsing JSON: ${error}`);
                }
            });
        }).on('error', (err) => {
            reject(`Request failed: ${err}`);
        });
    });
};

// Function to get and display all characters from the movie
const getMovieCharacters = async (movieId) => {
    const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

    try {
        // Fetch the film data
        const filmData = await fetchData(filmUrl);

        // Get the list of character URLs
        const characterUrls = filmData.characters;

        // Loop over character URLs and fetch the character names
        for (const url of characterUrls) {
            const characterData = await fetchData(url);
            console.log(characterData.name);
        }
    } catch (error) {
        console.error(`Error: ${error}`);
    }
};

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
    console.error('Usage: ./script.js <movie_id>');
    process.exit(1);
}

// Call the function to display the movie characters
getMovieCharacters(movieId);

