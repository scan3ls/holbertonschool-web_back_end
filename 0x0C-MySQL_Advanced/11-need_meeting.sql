-- Create VIEW need_meeting 
-- Lists all students that have a score under 80 and no last-meeting or more than 1 month

DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting
    AS SELECT
            name
        FROM
            students
        WHERE
            (score < 80 AND last_meeting IS NULL)
            OR
            (score < 80 AND DATEDIFF(CURDATE(), last_meeting) > 30);
