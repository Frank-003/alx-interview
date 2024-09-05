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
