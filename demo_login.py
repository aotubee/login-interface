#!/usr/bin/env python3
# coding=utf-8

import pymysql  
from pymysql import MySQLError  
  
# 数据库连接配置  
DB_CONFIG = {  
    'host': '$IP',  
    'user': 'root', 
    'password': '$PASS', 
    'database': 'testdb', 
    'charset': 'utf8mb4',  
    'cursorclass': pymysql.cursors.DictCursor  
}  
  
def create_connection():  
    """创建数据库连接"""  
    connection = None  
    try:  
        connection = pymysql.connect(**DB_CONFIG)  
        print("MySQL Database connection successful")  
    except MySQLError as e:  
        print(f"The error '{e}' occurred")  
    return connection  
  
def create_user(connection, username, password):  
    """创建新用户"""  
    try:  
        with connection.cursor() as cursor:  
            # SQL 插入语句  
            sql = "INSERT INTO user (username, password) VALUES (%s, %s)"  
            cursor.execute(sql, (username, password))  
          
        # 提交到数据库执行  
        connection.commit()  
        return True  
    except MySQLError as e:  
        print(f"Error: {e}")  
        return False  
  
def user_login(connection, username, password):  
    """用户登录"""  
    try:  
        with connection.cursor() as cursor:  
            # SQL 查询语句  
            sql = "SELECT * FROM user WHERE username = %s AND password = %s"  
            cursor.execute(sql, (username, password))  
            result = cursor.fetchone()  
            return result is not None  
    except MySQLError as e:  
        print(f"Error: {e}")  
        return False  
  
def main():  
    connection = create_connection()  
  
    if connection:  
        while True:  
            username = input("Enter username: ")  
            password = input("Enter password: ")  
            if user_login(connection, username, password):
                print("登录成功。")  
            else:  
                print("登录失败,检查用户名或密码:")  
                create_user(connection, username, password)
 #           else:
 #               input("Enter exit: ")  
 #               break

        connection.close()  
        print("MySQL connection is closed")  
  
if __name__ == "__main__":  
    main()
