import mysql.connector

Shop = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass",
)
mycursor = Shop.cursor()

try:
    sql = "CREATE DATABASE Shop"
    mycursor.execute(sql)
except:
    print('WE have a database with the name already.')

products = """
            CREATE TABLE Products(
                product_id PRIMARY KEY INT auto-increment,
                prduct_name VARCHAR(255),
                category_id INT FOREIGN KEY,
                price INT,
                quantity INT
            )
"""

categories = """
            CREATE TABLE Categories(
                catagory_id PRIMARY KEY INT auto-increment,
                categories_name VARCHAR(255)
            )
"""
try:
    mysql.execute(products)
    mysql.execute(categories)
except:
    print('Such Tables Exist')

def add_product(product_id, product_name, category_id, price, quantity):
        try:
            sql = "INSERT INTO Products (product_id, product_name, category_id, price, quantity) VALUES (%s, %s, %s, %s, %s)"
            values = (product_id, product_name, category_id, price, quantity)
            mycursor.execute(sql, values)
            Shop.commit()
            print("The Data added Successfuly!")
        except:
            print('Faield to add.')

def add_category(category_id, category_name):
        try:
            sql = "INSERT INTO Categories (category_id, category_name) VALUES (%s, %s)"
            values = (category_id, category_name)
            mycursor.execute(sql, values)
            Shop.commit()
            print("ezafe shod !!?")
        except  Exception as e:
            print('nashod: ', e)


def remove_product(product_id):
    try:
        sql = "DELETE FROM Products WHERE product_id = %s"
        values = (product_id,)
        mycursor.execute(sql, values)
        Shop.commit()
        print("hazf shod !!?")
    except  Exception as e:
        print('nashod: ', e)

def remove_category(category_id):
    try:
        sql = "DELETE FROM Categories WHERE category_id = %s"
        values = (category_id,)
        mycursor.execute(sql, values)
        Shop.commit()
        print("hazf shod !!?")
    except  Exception as e:
        print('nashod: ', e)

def edit_product(product_id, product_name, category_id, price, quantity):
    try:
        sql = "UPDATE Products SET product_name = %s, category_id = %s , price = %s , quantity = %s  WHERE product_id = %s"
        values = (product_name, category_id, price, quantity, product_id)
        mycursor.execute(sql, values)
        Shop.commit()
        print("taghir kard !!?")
    except  Exception as e:
        print('nashod: ', e)

def edit_category(category_id, category_name):
    try:
        sql = "UPDATE Categories SET category_name = %s WHERE category_id = %s"
        values = (category_name, category_id)
        mycursor.execute(sql, values)
        Shop.commit()
        print("taghir kard !!?")
    except  Exception as e:
        print('nashod: ', e)

def search_products(name_or_category):
    values = ...
    sql = ...
    try:
        if type(name_or_category) == int:
            sql = "SELECT * FROM Products WHERE product_id = %s"
            values = (name_or_category,)
        elif type(name_or_category) == str:
            sql = "SELECT * FROM Products WHERE product_name LIKE %s"
            values = (name_or_category + '%',)
        mycursor.execute(sql, values)
        result = mycursor.fetchall()
        print("pyda shod")
        return result
    except  Exception as e:
        print('nashod: ', e)

def search_categories(category_name):
    try:
        sql = "SELECT * FROM Categories WHERE category_name LIKE %s"
        values = (category_name + '%',)
        mycursor.execute(sql, values)
        result = mycursor.fetchall()
        print("pyda shod")
        return result
    except  Exception as e:
        print('nashod: ', e)

def display_products(self):
    try:
        sql = "SELECT * FROM Products"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(*result, sep='\n')
    except  Exception as e:
        print('nashod: ', e)

def display_categories(self):
    try:
        sql = "SELECT * FROM Categories"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(*result, sep='\n')
    except  Exception as e:
        print('nashod: ', e)

def close(self):
    try:
        mycursor.close()
        Shop.close()
        print('tamam')
    except  Exception as e:
        print('nashod: ', e)
