
create table Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    email VARCHAR,
    city VARCHAR,
    state VARCHAR,
    signup_date DATE
)


create table Categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR
)


create table Products (
    product_id INT PRIMARY KEY,
    category_id INT,
    product_name VARCHAR,
    price DECIMAL
)


create table Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    status VARCHAR
)


create table Order_Items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL
)