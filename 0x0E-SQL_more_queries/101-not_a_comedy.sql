-- A script that lists all shows without the genre Comedy
-- in the database hbtn_0d_tvshows.
SELECT ts.title
FROM tv_shows AS ts
INNER JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id

INNER JOIN tv_genres AS tg
ON tsg.genre_id = tg.id

WHERE tg.name NOT IN (
	SELECT tg.name
	FROM tv_shows AS ts
	JOIN tv_show_genres AS tsg
	ON ts.id = tsg.show_id

	JOIN tv_genres AS tg
	ON tsg.genre_id = tg.id
	WHERE tg.name = 'Comdey')
GROUP BY title
ORDER BY title;
