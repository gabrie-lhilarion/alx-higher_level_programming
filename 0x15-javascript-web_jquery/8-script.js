$(document).ready(function () {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        type: 'GET',
        success: function (data) {
            var movies = data.results;
            $.each(movies, function (index, movie) {
                $('#list_movies').append('<li>' + movie.title + '</li>');
            });
        },
        error: function () {
            $('#list_movies').append('<li>Error fetching movies</li>');
        }
    });
});
