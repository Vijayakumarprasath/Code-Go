with monthly_mrr as (
select coustomer_id, month ,sum(coalesce(enter_mrr_revenue_gracepriod_net,0)+ coalesce(entering_mrr_revenue))as total_mrr 
                from cust_mrr_data group by coustomer_id, month	),
mrr_with_lag (
select coustomer_id, month ,total_mrr ,lag(total_mrr ) over (partition by customer_id order_by month ) as prev_tot_mrr 
from monthly_mrr ),
select coustomer_id, month,total_mrr, prev_tot_mrr from mrr_with_lag where prev_tot_mrr is not null and total_mrr < 0.5 * prev_tot_mrr


__________

create procedure mrr_types (
in i_month nvarchar(20),
out out_table table(cust_id nvarchar(50), month nvarchar(20), mrr_type nvarchar(20) )
language sqlscript
as 
begin 

out_result = select cust_id,month , case 
                                        when sum(coalesce(enter_mrr,0)) > sum(coalesce(exit_mrr,0)) 
										and sum(coalesce(exi_mrr,0)) = 0 then 'expansion' 
										
										when sum(coalesce(enter_mrr,0)) = 0 and sum(coalesce(exit_mrr,0)) > 0 
										and grace_priod = 1 then 'pending churn'
										
										when sum(coalesce(enter_mrr,0)) = 0 and sum(coalesce(exit_mrr,0)) = 0 
										and grace_priod = 1 then ' churn'
										
										when sum(coalesce(enter_mrr,0))  > sum(coalesce(exit_mrr,0)) and grace_priod = 2 
										or(
										when sum(coalesce(enter_mrr_grace_priod,0))  > sum(coalesce(exit_mrr,0)) 
										and grace_priod = 1) then ' retention/reactivation'
										when sum(coalesce(exit_mrr,0)) > 0 then ''
										
										then 'others'
										end as mrr_type from mrr_dts
										where mont = : i_month
										GROUP by cust_id,month ; 
end;										


select date_clm + interval 1 day as next_missing_days from d_table where not exit (
                                                                       select 1 from d_table where date_clm = date_clm + interval 1 day )





call mrr_types('2023-04')

Basic SQL Queries (1–10)
1. Second Highest Salary

sql
Copy
Edit
SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
2. Find Duplicate Records in a Table

sql
Copy
Edit
SELECT name, COUNT(*)
FROM students
GROUP BY name
HAVING COUNT(*) > 1;
3. Delete Duplicate Records but Keep One

sql
Copy
Edit
DELETE FROM employees
WHERE id NOT IN (
    SELECT MIN(id)
    FROM employees
    GROUP BY name, salary
);
4. Get Employees with Same Salary

sql
Copy
Edit
SELECT e1.*
FROM employees e1
JOIN employees e2 ON e1.salary = e2.salary AND e1.id <> e2.id;
5. Find Nth Highest Salary (e.g., 3rd Highest)

sql
Copy
Edit
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 2;
-- (OFFSET is N-1 for the Nth highest)
6. Find Departments with More Than 5 Employees

sql
Copy
Edit
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5;
7. Employees Who Earn More Than Their Manager

sql
Copy
Edit
SELECT e.*
FROM employees e
JOIN employees m ON e.manager_id = m.id
WHERE e.salary > m.salary;
8. Find Top 3 Salaries in Each Department (Using Window Function)

sql
Copy
Edit
SELECT *
FROM (
  SELECT *,
         DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank
  FROM employees
) ranked
WHERE rank <= 3;
9. Find Continuous Dates (Detect Missing Dates)

sql
Copy
Edit
SELECT date_column + INTERVAL 1 DAY AS missing_date
FROM your_table t
WHERE NOT EXISTS (
    SELECT 1 FROM your_table
    WHERE date_column = t.date_column + INTERVAL 1 DAY
);
10. Self Join to Find Mentor-Mentee Relationship

sql
Copy
Edit
SELECT a.name AS mentee, b.name AS mentor
FROM employees a
JOIN employees b ON a.manager_id = b.id;
Intermediate SQL Queries (11–20)
11. Find Employees Who Never Submitted a Timesheet

sql
Copy
Edit
SELECT e.id, e.name
FROM employees e
LEFT JOIN timesheets t ON e.id = t.employee_id
WHERE t.employee_id IS NULL;
12. Find the Total Salary Paid Per Department (Including Departments with No Employees)

sql
Copy
Edit
SELECT d.name, COALESCE(SUM(e.salary), 0) AS total_salary
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY d.name;
13. Find Employees Hired in Last 3 Months

sql
Copy
Edit
SELECT *
FROM employees
WHERE hire_date >= CURRENT_DATE - INTERVAL '3 MONTH';
14. Retrieve Continuous Login Streaks (Advanced)

sql
Copy
Edit
SELECT user_id, MIN(login_date) AS start_date, MAX(login_date) AS end_date
FROM (
  SELECT user_id, login_date,
         login_date - INTERVAL ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date) DAY AS grp
  FROM logins
) t
GROUP BY user_id, grp;
15. Find Customers Who Bought All Products

sql
Copy
Edit
SELECT customer_id
FROM purchases
GROUP BY customer_id
HAVING COUNT(DISTINCT product_id) = (SELECT COUNT(*) FROM products);
16. Pivot Table: Convert Rows to Columns

sql
Copy
Edit
SELECT 
    employee_id,
    MAX(CASE WHEN month = 'Jan' THEN salary END) AS jan_salary,
    MAX(CASE WHEN month = 'Feb' THEN salary END) AS feb_salary
FROM salaries
GROUP BY employee_id;
17. Calculate Running Total (Cumulative Sum)

sql
Copy
Edit
SELECT 
  employee_id,
  salary,
  SUM(salary) OVER (PARTITION BY department_id ORDER BY hire_date) AS running_total
FROM employees;
18. Find the Most Recent Record Per Group (Latest Order Per Customer)

sql
Copy
Edit
SELECT *
FROM (
  SELECT *,
         ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rn
  FROM orders
) t
WHERE rn = 1;
19. Transpose Columns to Rows (UNPIVOT)

sql
Copy
Edit
SELECT employee_id, 'jan' AS month, jan_salary AS salary FROM salary_table
UNION ALL
SELECT employee_id, 'feb', feb_salary FROM salary_table;
20. Count Number of Employees in Each Salary Range

sql
Copy
Edit
SELECT 
  CASE 
    WHEN salary < 50000 THEN 'Low'
    WHEN salary BETWEEN 50000 AND 100000 THEN 'Medium'
    ELSE 'High'
  END AS salary_range,
  COUNT(*) AS count
FROM employees
GROUP BY salary_range;
Advanced SQL Queries (21–30)
21. Find the Most Frequent Value in a Column

sql
Copy
Edit
SELECT product_id
FROM orders
GROUP BY product_id
ORDER BY COUNT(*) DESC
LIMIT 1;
22. Find Employees Who Have More Than One Department

sql
Copy
Edit
SELECT id, name
FROM employees
GROUP BY id, name
HAVING COUNT(DISTINCT department_id) > 1;
23. Find the Nth Highest Salary (Generalized Query)

sql
Copy
Edit
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET (n - 1);
-- Replace n with the desired rank
24. Get the First and Last Name of Employees with the Longest Tenure

sql
Copy
Edit
SELECT first_name, last_name
FROM employees
WHERE hire_date = (SELECT MIN(hire_date) FROM employees);
25. Find Employees Who Have Never Been Assigned to a Project

sql
Copy
Edit
SELECT name
FROM employees
WHERE id NOT IN (SELECT employee_id FROM projects);
26. Get the Department with the Highest Average Salary

sql
Copy
Edit
SELECT department_id
FROM employees
GROUP BY department_id
ORDER BY AVG(salary) DESC
LIMIT 1;
27. Find the Sum of Salaries for Each Department Excluding the Highest Salary

sql
Copy
Edit
SELECT department_id, SUM(salary) - MAX(salary) AS sum_excluding_highest
FROM employees
GROUP BY department_id;
28. Find Employees Who Joined After a Specific Employee

sql
Copy
Edit
SELECT name
FROM employees
WHERE join_date > (SELECT join_date FROM employees WHERE name = 'John Doe');
29. Get the Total Number of Employees in Each Department, Including Those with No Department

sql
Copy
Edit
SELECT department_id, COUNT(id) AS total_employees
FROM employees
GROUP BY department_id WITH ROLLUP;
30. Get Employees Whose Salary is Below the Average Salary in Their Department

sql
Copy
Edit
SELECT name
FROM employees e
WHERE salary < (SELECT AVG(salary) FROM employees WHERE department_id = e.department_id);


___________Snowflake - proc_____________


create or replace task item_consumption_tsk
warehouse = compute_wh
schedule = '4 minute'
when
system$stream_has_data('ch19.curated_zone.curated_item_stm')

merge into ch19.consumption_zone.item_dim item using ch19.curated_zone.curated_item_stm curated_item_stm on
item.item_id = curated_item_stm.item_id and
item.start_date = curated_item_stm.start_date and
item.item_desc = curated_item_stm.item_desc
when matched
and curated_item_stm. METADATA$ACTION = 'INSERT'
and curated_item_stm. METADATA$ISUPDATE = 'TRUE
then update set
item. end_date = curated_item_stm.end_date,
item.price = curated_item_stm.price,
item.item_class = curatel_item_stm.item_class,
item.item_category = curated_item_stm.item_category
when matched
and curated_item_stm. METADATA$ACTION = 'DELETE'
and curated_item_stm. METADATA$ISUPDATE = 'FALSE'
then update set
item.active_flag = 'N',
updated_timestamp = current_timestamp()
when not matched
and curated_item_stm. METADATASACTION = 'INSERT'
and curated_item_stm.METADATA$ISUPDATE = 'FALSE'
then
insert (
item_id,
item_desc,
start_date,
end_date,
price,
item_class,
item_category)

I