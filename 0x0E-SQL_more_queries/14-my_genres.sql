-- A script that uses the hbtn_0d_tvshows database to lists
-- all genres of the show Dexter.
SELECT tg.name
FROM tv_genres AS tg
LEFT JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id
LEFT JOIN tv_shows AS ts
ON ts.id = tsg.show_id
WHERE ts.title = 'Dexter'
GROUP BY name
ORDER BY name;
