-- point 17
-- list all genres not linked to the show Dexter Results must be sorted in ascending order by the genre name Each record should display: tv_genres.name You can use a maximum of two SELECT statement.
SELECT tv_genres.name 
FROM tv_genres
WHERE tv_genres.id NOT IN
(SELECT tv_genres.id
FROM tv_genres 
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter")
ORDER BY tv_genres.name;
