-- Table: Activity

-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | player_id    | int     |
-- | device_id    | int     |
-- | event_date   | date    |
-- | games_played | int     |
-- +--------------+---------+
-- (player_id, event_date) is the primary key (combination of columns with unique values) of this table.
-- This table shows the activity of players of some games.
-- Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.

-- Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to determine the number of players who logged in on the day immediately following their initial login, and divide it by the number of total players.

-- The result format is in the following example.
select round(
    count(distinct a2.player_id) / count(distinct a1.player_id),
    2
)as fraction from Activity a1
left join(
    select player_id, min(event_date) as first_login from Activity a2 group by player_id
) first_logins on a1.player_id = first_logins.player_id
left join Activity a2 on a2.player_id = first_logins.player_id and a2.event_date = date_add(first_logins.first_login, interval 1 day)

