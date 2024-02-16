-- Список курсів, які певному студенту читає певний викладач.
SELECT s.subject_, t.teacher, st.student AS students 
FROM mark_nnij AS m 
LEFT JOIN subject_nnij AS s ON m.id=m.student_nnij_id
LEFT JOIN teacher_nnij AS t ON m.id=s.teacher_nnij_id
LEFT JOIN student_nnij AS st ON m.id=m.student_nnij_id
GROUP BY s.id