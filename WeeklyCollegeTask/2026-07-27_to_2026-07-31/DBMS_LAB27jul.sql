CREATE TABLE STUDENT(
  stu_id INT PRIMARY KEY,
  stu_name VARCHAR(30),
  email VARCHAR(30)
);
CREATE TABLE INSTRUCTOR(
  inst_id INT PRIMARY KEY,
  inst_name VARCHAR(30)
);
CREATE TABLE COURSE(
  course_id INT PRIMARY KEY,
  stu_id INT,
  grade FLOAT,
  FOREIGN KEY (stu_id) REFERENCES STUDENT(stu_id)
);

-- displaying the table schema
DESC STUDENT;
DESC INSTRUCTOR;
DESC COURSE;

-- inserting values in student table
INSERT INTO STUDENT(stu_id,stu_name,email) values
(1,"Syantan","sayantan@gmail.com"),
(2,"Souma","souma@gmail.com"),
(3,"Sandip","sandip@gmail.com"),
(4,"Sanjit","sanjit@gmail.com"),
(5,"Shakshi","shakshi@gmail.com");

-- inserting values in instructor table
INSERT INTO INSTRUCTOR(inst_id,inst_name) values
(1,"Ankush"),
(2,"Anirudh"),
(3,"Anirban"),
(4,"Ankit"),
(5,"Akhilesh");

-- inserting values in course
INSERT INTO COURSE(stu_id,course_id,grade) values
(1,2,9.2),
(2,1,8.5),
(3,3,7.2),
(4,5,9.5),
(5,4,8.9);

-- displaying the tables after inserting values
SELECT * FROM STUDENT;
SELECT * FROM INSTRUCTOR;
SELECT * FROM COURSE;

-- showing student name and their grade together where the grade is more than 9.0
SELECT stu_name AS student_name,grade AS student_grade
FROM STUDENT s
INNER JOIN COURSE c
WHERE s.stu_id=c.stu_id AND c.grade > 9.0
ORDER BY c.grade DESC;


ALTER TABLE COURSE ADD COLUMN course_name VARCHAR(20);



-- UPDATE COURSE c SET c.course_name="CSE" WHERE c.course_id=1;
-- UPDATE COURSE c SET c.course_name="CSE-AI/ML" WHERE c.course_id=2;
-- UPDATE COURSE c SET c.course_name="CSE-CyberSecurity" WHERE c.course_id=3;
-- UPDATE COURSE c SET c.course_name="CSE-DataScience" WHERE c.course_id=4;
-- UPDATE COURSE c SET c.course_name="CSE" WHERE c.course_id=5;



-- UPDATE COURSE c 
-- SET c.course_name = CASE course_id
--     WHEN 1 THEN "CSE"
--     WHEN 2 THEN "CSE-AI/ML"
--     WHEN 3 THEN "CSE-CyberSecurity"
--     WHEN 4 THEN "CSE-DataScience"
--     WHEN 5 THEN "CSE"
-- END
-- WHERE course_id IN (
--   1,2,3,4,5
-- );


UPDATE COURSE c SET c.grade=9.1 WHERE c.course_id=4;


SELECT * from COURSE;

