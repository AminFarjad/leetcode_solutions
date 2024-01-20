# Write your MySQL query statement below

select name from employee where id in (select e.id from employee e inner join employee e1 on e.id=e1.managerId group by e.id having count(*)>=5);
