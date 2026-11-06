-- Write your query below
SELECT s.name
FROM sales_person s
WHERE s.sales_id NOT IN(
    SELECT o.sales_id
    FROM orders o
    JOIN company c ON o.com_id = c.com_id
    WHERE c.name = 'CRIMSON'
)