# Write your MySQL query statement below
-- select prices.product_id,round(sum(price*units)/sum(units),2) as average_price from prices left join unitssold on prices.product_id=unitssold.product_id where purchase_date between start_date and end_date group by prices.product_id;

select prices.product_id,ifnull(round(sum(price*units)/sum(units),2),0) as average_price from prices left join unitssold on prices.product_id=unitssold.product_id where purchase_date between start_date and end_date or purchase_date is null group by prices.product_id;
