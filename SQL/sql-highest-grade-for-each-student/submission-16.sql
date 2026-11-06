-- Write your query below
WITH max_exams AS (
SELECT e.student_id, e.exam_id, e.score
FROM exam_results e
JOIN (
    SELECT student_id, MAX(score) AS score
    FROM exam_results
    GROUP BY student_id
) AS m
ON e.student_id = m.student_id AND e.score = m.score)

SELECT me.student_id, me.exam_id, me.score FROM max_exams me
JOIN (
    SELECT student_id, MIN(exam_id) AS exam_id
    FROM max_exams GROUP BY student_id
) AS i
ON me.exam_id = i.exam_id and me.student_id = i.student_id
ORDER BY student_id