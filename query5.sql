-- Знайти які курси читає певний викладач.
SELECT t.teacher, s.subject_ AS subjects
FROM teacher_nnij AS t
INNER JOIN subject_nnij AS s ON t.id = s.teacher_nnij_id
