# Write your MySQL query statement below
-- select *,IFNULL(action,'none') as a,count(*) from signups left join confirmations on signups.user_id=confirmations.user_id group by a,signups.user_id;


select user_id,round(e1/e,2) as confirmation_rate from (select t1.user_id,e1,e from (select signups.user_id,IFnull(d,0) as e1 from signups left join  (select signups.user_id,count(*) as d from signups left join confirmations on signups.user_id=confirmations.user_id where action='confirmed' group by user_id)t on t.user_id=signups.user_id)t1 inner join (select signups.user_id,IFnull(d,0) as e from signups left join  (select signups.user_id,count(*) as d from signups left join confirmations on signups.user_id=confirmations.user_id group by user_id)t on t.user_id=signups.user_id)t2 on t1.user_id=t2.user_id)t;


