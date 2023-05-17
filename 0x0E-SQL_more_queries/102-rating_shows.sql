-- A script that lists all shows from hbtn_0d_tvshows_rate by their rating.
select ts.title, SUM(r.rate) AS rating
FROM tv_shows AS ts
JOIN tv_show_ratings AS r
ON ts.id = r.show_id

GROUP BY title
ORDER BY rating DESC;
