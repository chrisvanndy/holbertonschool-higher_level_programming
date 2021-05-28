-- script that lists all genres from database and displays count of shows linked to genre id
-- record should list tv_show_genre as genre and count of shows linked to it
-- first column must be called genre
-- second column must be called number_of_shows
-- genres with null are not shown
-- format: desc order by count of shows linked
-- select tv_genre.name count all instances as number_shows
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
-- FROM equals LEFT item
FROM tv_show_genres
LEFT JOIN tv_genres ON tv_genres.id = genre_id
GROUP BY genre_id ORDER BY number_of_shows DESC;
