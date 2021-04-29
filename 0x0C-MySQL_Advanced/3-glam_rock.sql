-- List Glam rock bands
-- Order by lifespan
SELECT
    band_name AS band_name
    ,(IFNULL(split, YEAR(CURDATE())) - formed) AS lifespan
    FROM
        metal_bands
    WHERE
        style LIKE '%Glam Rock%';
