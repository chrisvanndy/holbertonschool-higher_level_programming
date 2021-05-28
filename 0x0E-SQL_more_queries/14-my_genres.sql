-- script that uses database to list genres of Dexter
-- tv_shows table contains only one record where title = Dexter
-- but the id can be different
-- format ascending order by tv_genre.name
-- TV GENRE namd listed to output
SELECT tv_genres.name
-- LEFT LIST TV SHOWS will acces
FROM tv_shows 
-- RETURN matches from TV SHOWS where tv_show.id = tv_show_genre.show_id
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- RETURN matches 
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
