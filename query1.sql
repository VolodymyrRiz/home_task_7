-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT st.student, (mark1+mark2+mark3+mark4+mark5)/5 AS AVGMARK
FROM student_nnij AS st
LEFT JOIN mark_nnij AS m ON st.id=m.student_nnij_id
ORDER BY AVGMARK DESC
LIMIT 5