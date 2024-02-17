-- Знайти середній бал у групах з певного предмета.
SELECT sub.subject_, g.id AS groupID, AVG(mark1+mark2+mark3+mark4+mark5)/5 AS AVGMARK
FROM mark_nnij AS m
LEFT JOIN subject_nnij AS sub ON sub.id=m.subject_nnij_id
LEFT JOIN grups_nnij AS g ON g.id=sub.id
WHERE g.id IN (SELECT id
FROM grups_nnij
WHERE id=2)