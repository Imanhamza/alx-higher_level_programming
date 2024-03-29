-- A script that lists all genres from hbtn_0d_tvshows and
-- displays the number of shows linked to each.
SELECT tg.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS tg
JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id
WHERE tsg.show_id IS NOT NULL
GROUP BY tg.name
ORDER BY number_of_shows DESC;
