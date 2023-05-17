-- A script that lists all genres in the database
-- hbtn_0d_tvshows_rate by their rating.
SELECT tg.name, SUM(r.rate) AS rating
FROM tv_genres AS tg
JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id

JOIN tv_show_ratings AS r
ON tsg.show_id = r.show_id

GROUP BY name
ORDER BY rating DESC;
