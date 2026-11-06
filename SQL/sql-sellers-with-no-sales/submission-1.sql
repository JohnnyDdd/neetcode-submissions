-- Write your query below
SELECT seller_name
FROM seller
WHERE seller_id NOT IN(
    SELECT s.seller_id
    FROM seller s
    JOIN orders o
    ON s.seller_id = o.seller_id AND (sale_date >= '2020-01-01' AND sale_date < '2021-01-01')
)
ORDER BY seller_name