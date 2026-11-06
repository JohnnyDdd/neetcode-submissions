-- Write your query below
WITH SUB1 AS(
    SELECT
    e.left_operand,
    e.operator,
    e.right_operand,
    v.value AS left_val
    FROM expressions e JOIN variables v ON v.name = e.left_operand 
),
SUB2 AS(
    SELECT
    e.left_operand,
    e.operator,
    e.right_operand,
    e.left_val,
    v.value AS right_val
    FROM SUB1 e JOIN variables v ON v.name = e.right_operand
)

SELECT 
left_operand,
operator,
right_operand,
(CASE 
    WHEN operator = '>' THEN 
        (CASE WHEN left_val > right_val THEN true ELSE false END)
    WHEN operator = '=' THEN 
        (CASE WHEN left_val = right_val THEN true ELSE false END)
    WHEN operator = '<' THEN 
        (CASE WHEN left_val < right_val THEN true ELSE false END)
END) AS value
FROM SUB2
