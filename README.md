Flask Warehouse API

This is a simple Flask API for managing a warehouse database. The API supports basic operations for products, customers, staff, and orders. The database is MySQL-based and includes tables for products, customers, staffs, and orders.
Installation

    Make sure you have Python installed. If not, download and install it from python.org.

    Install the required packages by running:

    bash

pip install Flask Flask-MySQL

Set up your MySQL database and update the database configuration in the Flask app. The default configuration is as follows:

python

app.config['MYSQL_DATABASE_USER'] = 'hadi'
app.config['MYSQL_DATABASE_PASSWORD'] = 'hadi78'
app.config['MYSQL_DATABASE_DB'] = 'warehouse'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

Create the necessary tables and insert sample data by running the SQL script provided in the SQL section.

Run the Flask app:

bash

    python app.py

    The API will be available at http://127.0.0.1:5000/.

API Endpoints
Products

    GET /products: Retrieve all products.

    POST /products: Create a new product. Requires a JSON payload with name, price, and amount.

    GET /products/int:id: Retrieve a specific product by ID.

    DELETE /products/int:id: Delete a specific product by ID.

    PUT /products/int:id: Update a specific product by ID. Requires a JSON payload with the fields to be updated.

Customers

    GET /customers: Retrieve all customers.

    POST /customers: Create a new customer. Requires a JSON payload with first_name, last_name, street, postal_code, and age.

    GET /customers/int:id: Retrieve a specific customer by ID.

    DELETE /customers/int:id: Delete a specific customer by ID.

    PUT /customers/int:id: Update a specific customer by ID. Requires a JSON payload with the fields to be updated.

Staff

    GET /staff: Retrieve all staff members.

    POST /staff: Create a new staff member. Requires a JSON payload with first_name, last_name, employee_since, and age.

    GET /staff/int:id: Retrieve a specific staff member by ID.

    DELETE /staff/int:id: Delete a specific staff member by ID.

    PUT /staff/int:id: Update a specific staff member by ID. Requires a JSON payload with the fields to be updated.

Orders

    GET /orders: Retrieve all orders.

    POST /orders: Create a new order. Requires a JSON payload with product_id, customer_id, and staff_id.

    GET /orders/int:product_id: Retrieve orders for a specific product ID.

    GET /orders/int:pid/int:cid: Retrieve orders for a specific product and customer ID.

    DELETE /orders/int:pid/int:cid: Delete the latest order for a specific product and customer ID.

    PUT /orders/int:pid/int:cid: Update the staff member for a specific product and customer ID. Requires a JSON payload with staff_id.

Note

    Make sure to handle your database credentials securely, especially in production environments.
    This README assumes a development environment, and additional security measures should be taken for a production environment.
