WITH
  r_unique AS (
    SELECT right_value as r_value, COUNT(r_value) as r_count FROM INPUT GROUP BY r_value 
  )
SELECT
  SUM(
    input.left_value * r_unique.r_count 
  ) as answer
FROM
  input
LEFT JOIN
  r_unique
ON input.left_value = r_unique.r_value;
