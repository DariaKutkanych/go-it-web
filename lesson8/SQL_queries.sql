-- 5 студентов с наибольшим средним баллом по всем предметам.
SELECT s.name, AVG(m.mark) as average_mark FROM marks AS m
LEFT JOIN students AS s ON m.student_id = s.id
GROUP BY m.student_id
ORDER BY average_mark DESC
LIMIT 5;

--  1 студент с наивысшим средним баллом по одному предмету.
SELECT s.name AS student_name, j.name AS subject, t.name as teacher, MAX(m.mark) as max_mark 
FROM marks AS m
LEFT JOIN students AS s ON m.student_id = s.id
LEFT JOIN subjects AS j ON m.subject_id = j.id
LEFT JOIN teachers AS T ON j.teacher_id  = t.id;

-- средний балл в группе по одному предмету.
SELECT g.number as group_number, j.name as subject, ROUND(AVG(m.mark), 2) as average_mark
FROM marks AS m
LEFT JOIN subjects AS j ON m.subject_id = j.id
LEFT JOIN students AS s ON m.student_id = s.id
LEFT JOIN groups AS g ON s.group_id = g.id
GROUP BY group_number, subject;

-- Средний балл в потоке.
SELECT ROUND(AVG(mark), 2) AS average_stream_score FROM marks m;

-- Какие курсы читает преподаватель.
SELECT t.name as teacher, s.name as subject from subjects s
LEFT JOIN teachers t on s.teacher_id = t.id
ORDER BY teacher;

-- Список студентов в группе.
SELECT g.number as group_name, s.name as student_name FROM students as s 
LEFT JOIN groups as g ON s.group_id = g.id 
ORDER BY g.number, s.name;

-- Оценки студентов в группе по предмету.
SELECT g.number as group_number, s.name as student_name, j.name as subject, m.mark as mark
FROM marks AS m
LEFT JOIN subjects AS j ON m.subject_id = j.id
LEFT JOIN students AS s ON m.student_id = s.id
LEFT JOIN groups AS g ON s.group_id = g.id
GROUP BY group_number, student_name, subject, mark
ORDER BY group_number, student_name, subject, mark;

-- Оценки студентов в группе по предмету на последнем занятии.
SELECT g.number as group_number, s.name as student_name, j.name as subject, m.mark, MAX(m.date) as date
FROM marks AS m
LEFT JOIN subjects AS j ON m.subject_id = j.id
LEFT JOIN students AS s ON m.student_id = s.id
LEFT JOIN groups AS g ON s.group_id = g.id
GROUP BY group_number, student_name, subject
ORDER BY group_number, student_name, subject, mark;

-- Список курсов, которые посещает студент.
SELECT s.name as student, j.name as subject from students s 
LEFT JOIN marks AS m ON s.id = m.student_id 
LEFT JOIN subjects AS j ON m.subject_id = j.id
GROUP BY student, subject;

-- Список курсов, которые студенту читает преподаватель.
SELECT s.name as student, t.name as teacher, j.name as subject from students s 
LEFT JOIN marks AS m ON s.id = m.student_id 
LEFT JOIN subjects AS j ON m.subject_id = j.id
LEFT JOIN teachers AS t ON j.teacher_id = t.id
GROUP BY student, teacher, subject;

-- Средний балл, который преподаватель ставит студенту.
SELECT s.name as student, t.name as teacher, ROUND(AVG(m.mark),2) as avg_mark from students s 
LEFT JOIN marks AS m ON s.id = m.student_id 
LEFT JOIN subjects AS j ON m.subject_id = j.id
LEFT JOIN teachers AS t ON j.teacher_id = t.id
GROUP BY student, teacher;

-- Средний балл, который ставит преподаватель.
SELECT t.name as teacher, ROUND(AVG(m.mark), 2) as avg_mark from marks as m
LEFT JOIN subjects s ON m.subject_id = s.id
LEFT JOIN teachers t ON s.teacher_id = t.id 
GROUP BY teacher;