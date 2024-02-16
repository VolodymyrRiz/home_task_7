-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT st.student, AVG(m.mark) as averageMark
FROM student_nnij AS st
LEFT JOIN mark_nnij AS m ON st.id=m.student_nnij_id
GROUP BY st.id
HAVING st.id < 6