from flask import Flask, request, jsonify
from flaskext.mysql import MySQL

import json


app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'hadi'
app.config['MYSQL_DATABASE_PASSWORD'] = 'hadi78'
app.config['MYSQL_DATABASE_DB'] = 'warehouse' 
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'


mysql.init_app(app) 
conn = mysql.connect()
 
@app.route('/products', methods = ['GET', 'POST'])
def products():
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute('SELECT * FROM products')
        res = cursor.fetchall()
        return jsonify(res) 
    if request.method == 'POST':
        req = request.get_json()
        query = (
                "INSERT INTO products (name, price, amount)"
                "VALUES (%s, %s, %s);"
        )
        data = (req['name'], req['price'], req['amount'])
        cursor.execute(query, data) 
        if cursor is not None:
            res = cursor.fetchone()
            print(res)
            return "Created", 201



@app.route('/products/<int:id>', methods = ['GET', 'DELETE', 'PUT'])
def get_product_1(id):
    cursor = conn.cursor()
    product = None
    if request.method == 'GET':
        cursor.execute('SELECT * FROM products LIMIT 1;')
        res = cursor.fetchone()
        for r in res:
            product = r 
        if product is not None:
            return jsonify(res)
        else:
            return "Not find", 404 
    if request.method == 'DELETE':
        query = """ DELETE FROM products WHERE id = {} """.format(id) 
        cursor.execute(query)
        return "The product with id = {} has been deleted!".format(id) 
    if request.method == 'PUT':
        req = request.get_json()
        query = "UPDATE products SET price = %s, amount = %s WHERE id = {};".format(id) 
        data = (req['price'], req['amount'])
        cursor.execute(query, data)   
        if cursor is not None:
            res = cursor.fetchone()
            print(res)
        return "The product with id = {} has been updated!".format(id, 200) 


@app.route('/customers', methods = ['GET', 'POST'])
def get_customer():
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute('SELECT * FROM customers')
        res = cursor.fetchall()
        return jsonify(res) 
    if request.method == 'POST':
        req = request.get_json()
        if req is not None:
            query = (
                    "INSERT INTO customers (first_name, last_name, street, postal_code, age)"
                    "VALUES (%s, %s, %s, %s, %s);"   
            )
            data = (req['first_name'], req['last_name'], req['street'], req['postal_code'], req['age'])
            cursor.execute(query, data)
            if cursor is not None:
                res = cursor.fetchone()
                print(res)
            return "Created", 201 



@app.route('/customers/<int:id>', methods = ['GET', 'DELETE', 'PUP'])
def customer(id):
    cursor = conn.cursor() 
    if request.method == 'GET':
        query = """SELECT * FROM customers WHERE id={};""".format(id) 
        cursor.execute(query) 
        res = cursor.fetchall()
        return jsonify(res), 200
    if request.method == 'DELETE':
        query = """ DELETE FROM customers WHERE id= {}""".format(id) 
        cursor.execute(query) 
        return "Customer with id = {} has been deleted".format(id) 
    ###### Problem ######
    if request.method == 'PUT':
        req = request.get_json()
        cursor.execute("UPDATE customers SET age = %s WHERE id = {}:".format(req['age'], id)   
        return jsonify(req), 200 


@app.route('/staff', methods = ['GET', 'POST'])
def staff():
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute('SELECT * FROM staffs')
        res = cursor.fetchall()
        return jsonify(res)
    if request.method == 'POST':
        req = request.get_json() 
        if req is not None:
            query = (
                "INSERT INTO staffs(first_name, last_name, employee_since, age) "
                "VALUES (%s, %s, %s, %s);"
            )
            data = (req['first_name'], req['last_name'], req['employee_since'], req['age'])
            cursor.execute(query, data) 
            if cursor is not None:
                res = cursor.fetchone()
                print(res)
            return "Created", 201



@app.route('/staff<int:id>', methods = ['GET', 'DELETE', 'PUT'])
def dstaff(id):
    cursor = conn.cursor()
    json = request.get_json()
    if request.method == 'GET':
        query = 'SELECT * FROM staffs WHERE id = {};'.format(id) 
        cursor.execute(query) 
        res = cursor.fetchall()
        return jsonify(res) 
    if request.method == 'DELETE':
        query = " DELETE FROM staffs WHERE id = {};".format(id) 
        cursor.execute(query) 
        return "Staff with id = {} has been deleted".format(id) 
    if request.method == 'PUT':
        last_name = request.form['last_name']
        query = (
            "UPDATE staffs SET last_name = {} WHERE id = {};".format(last_name, id)
        )
        cursor.execute(query, last_name)
        return "Staff with id = {} updated!".format(id)  



@app.route('/orders', methods = ['GET', 'POST'])
def order():
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute('SELECT * FROM orders')
        res = cursor.fetchall()
        return jsonify(res)
    if request.method =='POST':
        req = request.get_json() 
        if req is not None:
            query = (
                "INSERT INTO orders (product_id, customer_id, staff_id)"
                "VALUES (%s, %s, %s);"
            )
            data = (req['product_id'], req['customer_id'], req['staff_id'])
            cursor.execute(query, data)
            if cursor is not None:
                res = cursor.fetchone()
                print(res) 
            return "Created", 201


@app.route('/orders<int:product_id>', methods = ['GET'])
def get_order(product_id):
    if request.method == 'GET':
        cursor = conn.cursor() 
        cursor.execute('SELECT * FROM orders WHERE product_id = {};'.format(product_id))
        if res is not None:
            res = curosr.fetchall()
            print(res) 
        return jsonify(res), 200



@app.route('/orders<int:pid>/<int:cid>', methods = ['GET', 'DELETE', 'PUT'])
def get_orders(pid, cid):
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM orders WHERE product_id ={} AMD customer_id={};".format(pid, cid))
        res = cursor.fetchall()
        for row in res:
            print(row) 
        return jsonify(res) 
 
    if request.method == 'DELETE':
        query = """DELETE FROM orders WHERE product_id={} AND 
                    customer_id ={} ORDER BY created_at DESC LIMIT 1;
                """.format(pid, cid) 
        cursor.execute(query) 
        cursor.fetchall()
        return "Order with product_id {} and customer_id {} deleted".format(pid, cid), 200
 
    if request.method == 'PUT':
        req = request.get_json() 
        query = ("UPDATE orders SET staff_id = %s WHERE product_id = %s AND customer_id = %s;".format(pid, cid))
        data = (req['staff_id'], req['product_id'], req['customer_id'])
        cursor.execute(query, data) 
        if cursor is not None:
            res = cursor.fetchall()
            print(res) 
        return jsonify(res), 200



if __name__ == "__main__":
    app.run(debug=True)
