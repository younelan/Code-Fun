| Title                                     | Description                                                                                                   | Examples                                                                                             | Tests                                                                                   |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Retrieve Specific Data                    | Retrieve all employees who joined after January 1st, 2023, from an "Employees" table.                         | `SELECT * FROM Employees WHERE join_date > '2023-01-01';`                                              | (Syntax and logic check)                                                                 |
| Calculate Total Sales                     | Calculate the total sales amount for each product category from an "Orders" table.                            | `SELECT category, SUM(amount) AS total_sales FROM Orders GROUP BY category;`                           | (Aggregate function and grouping check)                                                    |
| Find Employees in Department              | Retrieve all employees who belong to the "Marketing" department from an "Employees" table.                    | `SELECT * FROM Employees WHERE department = 'Marketing';`                                               | (Syntax and logic check)                                                                 |
| List Top 5 Customers by Orders            | List the top 5 customers who placed the most orders, along with their total order count, from an "Orders" table. | `SELECT customer_id, COUNT(*) AS order_count FROM Orders GROUP BY customer_id ORDER BY order_count DESC LIMIT 5;` | (Sorting and limit check)                                                                |
| Calculate Average Order Value             | Calculate the average order value for each month in 2023 from an "Orders" table.                              | `SELECT MONTH(order_date) AS month, AVG(order_value) AS avg_order_value FROM Orders WHERE YEAR(order_date) = 2023 GROUP BY MONTH(order_date);` | (Date functions and aggregate check)                                                      |
| Retrieve Latest Order Date by Customer    | Retrieve the latest order date for each customer from an "Orders" table.                                      | `SELECT customer_id, MAX(order_date) AS latest_order_date FROM Orders GROUP BY customer_id;`            | (Aggregate function check)                                                               |
| Identify Customers with Multiple Orders   | List all customers who placed more than 3 orders in January 2023 from an "Orders" table.                       | `SELECT customer_id, COUNT(*) AS order_count FROM Orders WHERE MONTH(order_date) = 1 AND YEAR(order_date) = 2023 GROUP BY customer_id HAVING COUNT(*) > 3;` | (Grouping and filtering check)                                                           |
| Calculate Revenue Growth                 | Calculate the year-over-year revenue growth percentage from 2022 to 2023 from an "Revenue" table.              | `SELECT (SUM(revenue_2023) - SUM(revenue_2022)) / SUM(revenue_2022) * 100 AS revenue_growth FROM Revenue;` | (Mathematical calculation check)                                                         |
| List Inactive Customers                  | List customers who haven't placed any orders in the last 6 months from an "Customers" and "Orders" table.     | ```sql
  SELECT c.customer_id, c.customer_name
  FROM Customers c
  LEFT JOIN Orders o ON c.customer_id = o.customer_id
  WHERE o.order_date IS NULL OR o.order_date < DATE_SUB(CURDATE(), INTERVAL 6 MONTH);
  ```                                                                                                       | (Left join and date functions check)                                                      |
| Find Popular Products                    | Identify products that have been ordered more than 100 times from an "Orders" and "Products" table.           | ```sql
  SELECT p.product_id, p.product_name, COUNT(*) AS order_count
  FROM Orders o
  JOIN Products p ON o.product_id = p.product_id
  GROUP BY p.product_id, p.product_name
  HAVING COUNT(*) > 100;
  ```                                                                                                       | (Join, grouping, and aggregate function check)                                            |
| Calculate Employee Salaries              | Calculate the total salary expense per department from an "Employees" table.                                  | `SELECT department, SUM(salary) AS total_salary FROM Employees GROUP BY department;`                   | (Aggregate function and grouping check)                                                    |
| Identify Duplicate Entries               | Identify duplicate email addresses in an "Customers" table.                                                    | `SELECT email, COUNT(*) AS duplicate_count FROM Customers GROUP BY email HAVING COUNT(*) > 1;`          | (Grouping and duplicate detection check)                                                  |
| Update Records Based on Condition        | Update the salary of all employees who have been with the company for more than 5 years in an "Employees" table. | ```sql
  UPDATE Employees
  SET salary = salary * 1.1
  WHERE DATEDIFF(CURDATE(), join_date) > 1825;
  ```                                                                                                       | (Update statement and date functions check)                                               |
| Calculate Customer Lifetime Value        | Calculate the average lifetime value of customers based on their total spending from an "Orders" table.       | `SELECT AVG(total_spending) AS avg_lifetime_value FROM (SELECT customer_id, SUM(order_value) AS total_spending FROM Orders GROUP BY customer_id) AS customer_spending;` | (Subquery and aggregate function check)                                                   |
| Rank Customers by Order Frequency        | Rank customers based on the number of orders they've placed in descending order from an "Orders" table.       | ```sql
  SELECT customer_id, COUNT(*) AS order_count,
         RANK() OVER (ORDER BY COUNT(*) DESC) AS customer_rank
  FROM Orders
  GROUP BY customer_id;
  ```                                                                                                       | (Window function and ranking check)                                                       |
| Identify Cross-Selling Opportunities     | List products frequently bought together based on order history from an "Orders" table.                       | ```sql
  SELECT p1.product_id AS product1, p2.product_id AS product2, COUNT(*) AS order_count
  FROM Orders o1
  JOIN Orders o2 ON o1.order_id = o2.order_id AND o1.product_id < o2.product_id
  JOIN Products p1 ON o1.product_id = p1.product_id
  JOIN Products p2 ON o2.product_id = p2.product_id
  GROUP BY p1.product_id, p2.product_id
  HAVING COUNT(*) > 10;
  ```                                                                                                       | (Self-join and correlation check)                                                         |
| Find Orders with Missing Customer Info   | Identify orders with missing customer information (e.g., customer_id is null) from an "Orders" table.         | `SELECT * FROM Orders WHERE customer_id IS NULL;`                                                     | (Null check)                                                                            |
| Calculate Moving Average                 | Calculate the 7-day moving average of daily sales from a "Sales" table.                                       | ```sql
  SELECT sales_date, daily_sales,
         AVG(daily_sales) OVER (ORDER BY sales_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_average
  FROM Sales;
  ```                                                                                                       | (Window function and moving average check)                                                 |
| Find Incomplete Orders                   | List orders that are missing order details (e.g., shipping address) from an "Orders" table.                   | `SELECT * FROM Orders WHERE shipping_address IS NULL;`                                                | (Null check)                                                                            |
| Identify Peak Sales Periods              | Identify months with the highest sales revenue from an "Orders" table.                                        | ```sql
  SELECT DATE_FORMAT(order_date, '%Y-%m') AS month_year, SUM(order_amount) AS total_sales
  FROM Orders
  GROUP BY DATE_FORMAT(order_date, '%Y-%m')
  ORDER BY total_sales DESC
  LIMIT 1;
  ```                                                                                                       | (Date functions and aggregation check)                                                    |
| Calculate Order Conversion Rate          | Calculate the conversion rate of orders to purchases from an "Orders" and "Visitors" table.                   | ```sql
  SELECT COUNT(DISTINCT o.order_id) / COUNT(DISTINCT v.visitor_id) AS conversion_rate
  FROM Visitors v
  LEFT JOIN Orders o ON v.visitor_id = o.visitor_id;
  ```                                                                                                       | (Conversion calculation and left join check)                                              |
| Find Customers with High Spending         | Identify customers who spent more than $10,000 in total from an "Orders" table.                               | ```sql
  SELECT customer_id, SUM(order_amount) AS total_spending
  FROM Orders
  GROUP BY customer_id
  HAVING SUM(order_amount) > 10000;
  ```                                                                                                       | (Grouping and aggregate function check)                                                   |
| Update Records with Subquery             | Update product prices to include a 10% discount for products in a specific category from a "Products" table.   | ```sql
  UPDATE Products
  SET price = price * 0.9
  WHERE category = 'Electronics';
  ```                                                                                                       | (Update statement with subquery check)                                                    |
| Calculate Running Total                  | Calculate the running total of sales revenue for each day from a "Sales" table.                                | ```sql
  SELECT sales_date, sales_amount,
         SUM(sales_amount) OVER (ORDER BY sales_date) AS running_total
  FROM Sales;
  ```                                                                                                       | (Window function and running total check)                                                 |
| Retrieve Nested JSON Data                | Retrieve data from a column containing nested JSON structures in a "Customers" table.                         | ```sql
  SELECT customer_id, JSON_EXTRACT(customer_data, '$.name') AS customer_name
  FROM Customers;
  ```                                                                                                       | (JSON extraction function check)                                                          |
| Identify Slowest Performing Queries      | Identify the top 5 slowest performing queries based on execution time from a query execution log table.       | ```sql
  SELECT query_id, query_text, execution_time
  FROM QueryLogs
  ORDER BY execution_time DESC
  LIMIT 5;
  ```                                                                                                       | (Query execution time and ordering check)                                                 |
| Find Customers with Longest Tenure        | Identify customers who have been with the company for more than 5 years based on their first order date from an "Orders" table. | ```sql
  SELECT customer_id, MIN(order_date) AS first_order_date
  FROM Orders
  GROUP BY customer_id
  HAVING DATEDIFF(CURDATE(), MIN(order_date)) > 1825;
  ```                                                                                                       | (Date functions and tenure calculation check)                                            |
| Calculate Customer Retention Rate        | Calculate the customer retention rate for a given year based on repeat purchases from an "Orders" table.     | ```sql
  SELECT COUNT(DISTINCT customer_id) / COUNT(DISTINCT first_order_year) AS retention_rate
  FROM Orders
  WHERE YEAR(order_date) = :year;
  ```                                                                                                       | (Retention rate calculation check)                                                       |

