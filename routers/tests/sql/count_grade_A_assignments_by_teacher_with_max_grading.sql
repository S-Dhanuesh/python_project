SELECT teacher_id, COUNT(*) AS grade_a_count
FROM Assignments
WHERE grade = 'A'
GROUP BY teacher_id
ORDER BY grade_a_count DESC
LIMIT 1;