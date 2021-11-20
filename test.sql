--Get the total money earned and the average order value for the month of March.
select sum(order_value), avg(order_value)
from sales_order
where month(created_at) = 3;

--What was the month with the most orders?
select sum(id_order), created_at --count, created_at should be at month  level
from sales_order
group by id_order, created_at
order by id_order desc

select count(*) from sales_order


--For March 2020 what was the id_order with the highest order value
select id_order
from sales_order
where month(created_at) = 3 and year(created_at) = '2020' and order_value=max(order_value)