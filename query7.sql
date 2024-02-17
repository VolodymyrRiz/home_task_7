-- Знайти оцінки студентів у окремій групі з певного предмета.
SELECT st.student, sub.subject_, m.mark1 AS Mark1, m.mark2 AS Mark2, m.mark3 AS Mark3, m.mark4 AS Mark4, m.mark5 AS Mark5
FROM student_nnij AS st
JOIN subject_nnij AS sub ON sub.id=1
LEFT JOIN mark_nnij AS m ON st.id=m.id
WHERE st.grups_nnij_id IN (SELECT id
FROM grups_nnij
WHERE name_="0")
