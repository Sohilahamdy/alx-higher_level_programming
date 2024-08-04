-- List genres not linked to the show Dexter
SELECT tg.name
FROM tv_genres tg
WHERE tg.id NOT IN (
    SELECT tsg.genre_id
    FROM tv_show_genres tsg
    JOIN tv_shows ts ON ts.id = tsg.show_id
    WHERE ts.title = 'Dexter'
)
ORDER BY tg.name;
