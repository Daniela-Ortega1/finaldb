-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS telepizzadaniela;
USE telepizzadaniela;

-- Crear la tabla stores primero
CREATE TABLE IF NOT EXISTS stores (
    store_id INT AUTO_INCREMENT PRIMARY KEY,
    store_name VARCHAR(50),
    address VARCHAR(100),
    city VARCHAR(50)
);

-- Crear la tabla employees después
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    position VARCHAR(50),
    hire_date DATE,
    salary DECIMAL(10, 2),
    store_id INT,
    CONSTRAINT fk_employees_stores FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

-- Crear la tabla customers
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    gender VARCHAR(10),
    age INT,
    city VARCHAR(50)
);

-- Crear la tabla pqrs
CREATE TABLE IF NOT EXISTS pqrs (
    pqrs_id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(50),
    case_date DATE,
    subject VARCHAR(200),
    status VARCHAR(50),
    urgency VARCHAR(50),
    customer_id INT,
    CONSTRAINT fk_pqrs_customers FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Crear la tabla orders
CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    payment_method VARCHAR(20),
    customer_id INT,
    store_id INT,
    CONSTRAINT fk_orders_customers FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CONSTRAINT fk_orders_stores FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

-- Crear la tabla products
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(50),
    price DECIMAL(10, 2)
);

1. customer
2. store
3. product
4. employee
5. order
6. pqrs