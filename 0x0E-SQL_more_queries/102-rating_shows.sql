-- point 19
-- lists all shows from hbtn_0d_tvshows_rate Each record should display: tv_shows.title - rating sum Results must be sorted in descending order by the rating
SELECT tv_shows.title, COUNT(tv_show_ratings.rate) AS rating
FROM tv_show_ratings
RIGHT JOIN tv_shows
ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title, tv_show_ratings.show_id
ORDER BY rating DESC;
