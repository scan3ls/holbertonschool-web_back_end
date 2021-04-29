-- Create Index idx_name_first_score
-- Index on table names and the first letter of name and score

CREATE
    INDEX idx_name_first_score
        ON names (name(1), score);
