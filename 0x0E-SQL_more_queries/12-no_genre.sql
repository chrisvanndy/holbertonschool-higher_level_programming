-- write a script that lists all shows contained in database
-- output: tv_shows.title - tv_show_genres.genre_id
-- output: tv_shows.title ascending and tv_show_genres.genre_id
SELECT s.`title`, g.`genre_id`
FROM `tv_shows` AS s
-- tv_show attr name id(primarykey) tv_show_genre attr show id(fk?) genre_id)
-- tv_show.id and tv_show_genre.show_id ( are  == ) inner join these attrs
	LEFT JOIN `tv_show_genres` AS g ON s.`id` = g.`show_id`
	-- left join includes values that contain null
	WHERE g.`genre_id` IS NULL
	-- only list items WHERE the genre_id IS NULL
ORDER BY s.`title`, g.`genre_id`;
