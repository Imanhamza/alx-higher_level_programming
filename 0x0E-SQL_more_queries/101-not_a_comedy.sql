-- A script that lists all shows without the genre Comedy
-- in the database hbtn_0d_tvshows.
SELECT DISTINCT ts.title
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id

LEFT JOIN tv_genres AS tg
ON tsg.genre_id = tg.id

WHERE ts.id NOT IN (
	SELECT ts.id
	FROM tv_shows AS ts
	LEFT JOIN tv_show_genres AS tsg
	ON ts.id = tsg.show_id

	LEFT JOIN tv_genres AS tg
	ON tsg.genre_id = tg.id
	WHERE tg.name = 'Comdey')

ORDER BY title;
