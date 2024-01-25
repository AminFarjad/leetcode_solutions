-- # Write your MySQL query statement below
select project_id,round(sum(experience_years)/count(*),2)as average_years from project natural join (select * from employee where experience_years is not null)t group by project_id;


