-- Знайти середній бал на потоці (по всій таблиці оцінок).
SELECT AVG(mark1+mark2+mark3+mark4+mark5)/5 AS averageMark
FROM mark_nnij