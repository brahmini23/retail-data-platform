Retail Data Platform Database

Tables:

Customers
---------
customer_id (PK)
first_name
last_name
email
city
state
signup_date

Categories
---------
category_id (PK)
category_name

Products
---------
product_id (PK)
category_id (FK)
product_name
price

Orders
---------
order_id (PK)
customer_id (FK)
order_date
status

Order_Items
---------
order_item_id (PK)
order_id (FK)
product_id (FK)
quantity
unit_price