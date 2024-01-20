-- # Write your MySQL query statement below


-- select *, IfNULL(t.subject_name, 'ss') as d,count(null) from subjects,students left join( select * from examinations)t on t.student_id=students.student_id where t.subject_name = subjects.subject_name or t.subject_name is null group by students.student_id,subjects.subject_name order by students.student_id;

-- select *,count(*) from subjects,students left join examinations on students.student_id= examinations.student_id where examinations.subject_name=subjects.subject_name or examinations.subject_name is null group by subjects.subject_name,students.student_id order by students.student_id,subjects.subject_name

select s.student_id,s.student_name,s.subject_name,ifnull(attended_exams,0) as attended_exams from (select * from 
subjects,students)s left join 
(select *,count(*) as attended_exams from examinations group by student_id,subject_name)t
on s.student_id=t.student_id and s.subject_name=t.subject_name order by s.student_id,s.subject_name;
