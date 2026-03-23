
-- select stu.student_id,stu.student_name,sub.subject_name from students as stu 
--     cross join subjects as sub on 1 = 1
--     left join examinations as exam on stu.student_id = exam.student_id

select stu.student_id,stu.student_name, sub.subject_name,count(exam.student_id) as attended_exams from Subjects as sub 
    cross join students as stu 
    left join examinations as exam on stu.student_id = exam.student_id and sub.subject_name = exam.subject_name
    group by stu.student_id,stu.student_name,sub.subject_name
    order by stu.student_id,stu.student_name,sub.subject_name;
