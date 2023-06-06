CREATE DATABASE classroom;

use classroom;

create table science_class (
	enrollment_no int,
    full_name varchar(20),
    science_marks int
    ); 
select * from science_class;

INSERT INTO science_class(enrollment_no, full_name, science_marks)
	values (1,'popeye', 33),(2,'olive', 54),(3,'brutus', 98);


copy science_class FROM ‘C:\Users\Nish anth\Desktop\360DigiTMG Assignments and Study Material\S Q L\Assignments_03_SQL_dataset\Assignments_03_SQL_dataset\STUDENT.CSV’ CSV HEADER;    


SELECT * 
FROM Science_Class;

SELECT full_name
FROM Science_Class
WHERE science_marks > 60;

SELECT * 
FROM students 
WHERE science_marks BETWEEN 35 AND 60;
    
SELECT * 
FROM science_class 
WHERE science_marks <= 35 OR science_marks >= 60;

UPDATE science_class
SET science_marks= 45
 	WHERE name = 'Popeye';


DELETE from science_class
WHERE name = 'Robb';

alter table science_class rename full_name to student_name;
