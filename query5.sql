-- Знайти які курси читає певний викладач.
SELECT t.teach_name, s.subj_name AS subjects
FROM teachers AS t
INNER JOIN subjects AS s ON t.id = s.teacher_id
