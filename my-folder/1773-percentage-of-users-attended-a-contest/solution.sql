# Write your MySQL query statement below
-- select *,count(register.user_id)/count(distinct(users.user_id)) from users left join register on users.user_id=register.user_id group by contest_id;

select contest_id,round((count(user_id)/e)*100,2) as percentage from register,(select count(*) as e from users)t group by contest_id order by percentage desc,contest_id;


