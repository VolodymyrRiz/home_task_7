-- Table: groups_nnij
DROP TABLE IF EXISTS grups_nnij;
CREATE TABLE grups_nnij (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_ VARCHAR(3) UNIQUE NOT NULL
);

-- Table: students_nnij
DROP TABLE IF EXISTS student_nnij;
CREATE TABLE student_nnij (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student VARCHAR(30) UNIQUE NOT NULL,
    grups_nnij_id INTEGER,
    FOREIGN KEY (grups_nnij_id) REFERENCES grups_nnij (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Table: teachers_nnij
DROP TABLE IF EXISTS teacher_nnij;
CREATE TABLE teacher_nnij (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher VARCHAR(5) UNIQUE NOT NULL,
    grups_nnij_id INTEGER,
    FOREIGN KEY (grups_nnij_id) REFERENCES grups_nnij (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Table: subjects_nnij
DROP TABLE IF EXISTS subject_nnij;
CREATE TABLE subject_nnij (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_ VARCHAR(5) UNIQUE NOT NULL,
    teacher_nnij_id INTEGER,
    FOREIGN KEY (teacher_nnij_id) REFERENCES teacher_nnij (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Table: marks_nnij
DROP TABLE IF EXISTS mark_nnij;
CREATE TABLE mark_nnij (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_nnij_id INTEGER,
    subject_nnij_id INTEGER,
    mark1 INTEGER,
    mark2 INTEGER,
    mark3 INTEGER,
    mark4 INTEGER,
    mark5 INTEGER,
    FOREIGN KEY (student_nnij_id) REFERENCES student_nnij (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
    FOREIGN KEY (subject_nnij_id) REFERENCES subject_nnij (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);
