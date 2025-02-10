SELECT grade, COUNT(*) AS assignment_count
FROM Assignments
GROUP BY grade;