-- Create Trigger on email change
-- Reset valid_email
DROP TRIGGER IF EXISTS unvalidate_email;
DELIMITER //
CREATE
    TRIGGER unvalidate_email
    BEFORE UPDATE ON users
    FOR EACH ROW
    BEGIN
        IF OLD.email != NEW.email THEN
            SET NEW.valid_email = 0;
        END IF;
    END//
DELIMITER ;
