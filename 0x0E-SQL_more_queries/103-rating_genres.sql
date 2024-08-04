-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tg.name AS genre, COALESCE(SUM(tsr.rate), 0) AS rating
FROM tv_genres tg
LEFT JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
LEFT JOIN tv_show_ratings tsr ON tsg.show_id = tsr.show_id
GROUP BY tg.name
ORDER BY rating DESC;
