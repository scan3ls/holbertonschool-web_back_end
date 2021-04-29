-- Create Stored Procedure AddBonus
-- Insert new correction and create Project if Not Exists

DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER //

CREATE
    PROCEDURE AddBonus (
        IN user_id INT
       ,IN project_name CHAR(255)
       ,IN score INT
    )
    BEGIN
        DECLARE proj_ID INT DEFAULT 0;

        SELECT id
        INTO proj_ID
        FROM projects
        WHERE name = project_name;

        INSERT IGNORE INTO projects (id, name)
            VALUES (proj_ID, project_name);

        SELECT id
        INTO proj_ID
        FROM projects
        WHERE name = project_name;

        INSERT IGNORE INTO corrections (user_id, project_id, score)
            VALUES (user_id, proj_ID, score);
    END//

DELIMITER ;
