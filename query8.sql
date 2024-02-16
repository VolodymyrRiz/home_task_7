-- Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT Subj.subject_ AS Subject_, t.teacher AS Teacher, avg(m.mark) as averageMark
FROM subjecs_nnij AS Subj
LEFT JOIN mark_nnij AS m ON Subj.id=m.subject_nnij_id
LEFT JOIN teacher_nnij AS t ON t.id=Subj.id