-- A script that uses the hbtn_0d_tvshows database to list all
-- genres not linked to the show Dexter.
SELECT tg.name
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
	WHERE ts.title = 'Dexter')
GROUP BY name
ORDER BY tg.name;
