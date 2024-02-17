-- Знайти студента із найвищим середнім балом з певного предмета.
SELECT st.student, Subj.subject_ AS Subject_, (mark1+mark2+mark3+mark4+mark5)/5 AS AVGMARK
FROM student_nnij AS st
LEFT JOIN mark_nnij AS m ON st.id=m.student_nnij_id
LEFT JOIN subject_nnij AS Subj ON Subj.id=m.subject_nnij_id
WHERE st.id>=1 AND st.id<=30
GROUP BY Subj.id
ORDER BY AVGMARK DESC
LIMIT 1
