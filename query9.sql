-- Знайти список курсів, які відвідує студент.
SELECT m.subject_nnij_id, s.subject_, st.student
FROM mark_nnij AS m 
LEFT JOIN subject_nnij AS s ON s.id=m.subject_nnij_id
LEFT JOIN student_nnij AS st ON s.id=m.student_nnij_id
GROUP BY s.id