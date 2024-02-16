-- Знайти студента із найвищим середнім балом з певного предмета.
SELECT st.student, Subj.subject_ AS Subject_, AVG(m.mark) as averageMark
FROM student_nnij AS st
LEFT JOIN mark_nnij AS m ON st.id=m.student_nnij_id
LEFT JOIN subject_nnij AS Subj ON Subj.id=m.subject_nnij_id
WHERE st.id>=1 AND st.id<=30
GROUP BY Subj.id