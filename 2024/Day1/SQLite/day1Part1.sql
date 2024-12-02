WITH
  sorted_left AS (
    SELECT left_value, ROW_NUMBER() OVER (ORDER BY left_value) AS row_num
    FROM input
  ),
  sorted_right AS (
    SELECT right_value, ROW_NUMBER() OVER (ORDER BY right_value) AS row_num
    FROM input
  )
SELECT
  SUM(
    ABS(
      sorted_left.left_value - sorted_right.right_value
    )
  ) as answer
FROM
  sorted_left
JOIN
  sorted_right
ON sorted_left.row_num = sorted_right.row_num;
