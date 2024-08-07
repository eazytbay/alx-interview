const fetch = require('node-fetch');

async function getMovieCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error('Error: Unable to fetch data from the API');
    }

    const filmData = await response.json();
    const characterUrls = filmData.characters;

    for (const characterUrl of characterUrls) {
      const characterResponse = await fetch(characterUrl);
      if (characterResponse.ok) {
        const characterData = await characterResponse.json();
        console.log(characterData.name);
      }
    }
  } catch (error) {
    console.error(error.message);
  }
}

const args = process.argv.slice(2);
if (args.length !== 1) {
  console.log('Usage: node star_wars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = args[0];
getMovieCharacters(movieId);

