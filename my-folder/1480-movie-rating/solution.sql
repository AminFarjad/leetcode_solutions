-- # Write your MySQL query statement below
select name as results from (select name,count(*) from users inner join movierating 
where movierating.user_id = users.user_id 
group by movierating.user_id 
order by count(*) desc,name limit 1)t 
union all
select title as results from (select *,avg(rating) from movies natural join movierating 
where extract(month from created_at)=2 and extract(year from created_At)=2020 group by title order by avg(rating) desc,title limit 1) t1;
