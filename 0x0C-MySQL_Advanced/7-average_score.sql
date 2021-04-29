-- Create Stored procedure ComputeAverageScoreForUser
-- Compute and update average score for users from corrections

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //

CREATE
    PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
    BEGIN
        DECLARE average INT DEFAULT 0;

        SELECT
            AVG(score)
        INTO average
        FROM corrections
        WHERE
            corrections.user_id = user_id;

        UPDATE users
        SET
            average_score = average
        WHERE
            id = user_id;
    END//

DELIMITER ;