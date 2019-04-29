use GP;

insert into student values(1,'student1','student1','sh1@gmail.com','123456');
insert into student values(2,'student2','student2','sh2@gmail.com','123456');
insert into student values(3,'student3','student3','sh3@gmail.com','123456');
insert into student values(4,'student4','student4','sh4@gmail.com','123456');

insert into prof values(1,'prof1','prof1','sha1@gmail.com','123456');
insert into prof values(2,'prof2','prof2','sha2@gmail.com','123456');

insert into course values(1,'course1','1');
insert into course values(2,'course2','2');

insert into `day` values(1,'sat');
insert into `day` values(2,'sun');
insert into `day` values(3,'mon');

insert into class values(1,2,203);

insert into period values(1,'8:30','10:00');
insert into period values(2,'10:10','11:40');

insert into student_has_course values(1,1);
insert into student_has_course values(2,1);
insert into student_has_course values(3,2);
insert into student_has_course values(4,2);

insert into timetable values(1,1,1,1);
insert into timetable values(1,2,1,2);
insert into timetable values(2,1,1,1);
insert into timetable values(2,2,1,2);

select pid from period where starttime < '8:45' and endtime > '8:45';

select timetable.course_cid from timetable where day_did = 1 and class_cid = 1 and period_pid = 1;

insert into attendance values(1,1,str_to_date('24-4-2019','%d-%m-%Y'));
select * from attendance;