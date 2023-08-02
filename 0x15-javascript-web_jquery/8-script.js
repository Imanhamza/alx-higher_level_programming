const moviesList = $('#list_movies');
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.getJSON(url, function (data) {
  const movies = data.results;

  $.each(movies, function (index, movie) {
    moviesList.append('<li>' + movie.title + '</li>');
  });
});
