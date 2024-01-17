# Write your MySQL query statement
select a.machine_id,round(avg((a.timestamp-a1.timestamp)),3)as processing_time from activity a cross join activity a1 where a.process_id = a1.process_id and a1.activity_type != a.activity_type and a1.machine_id=a.machine_id and a.timestamp > a1.timestamp group by a.machine_id;
