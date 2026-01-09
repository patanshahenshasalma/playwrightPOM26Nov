# sqlite3 connections

# import sqlite3

# def test_sqlite_connection():
#    try:
#         dataTables = sqlite3.connect(r"path")
#         data = dataTables.cursor()
#         data.execute("select * from Album where AlbumId = 2")
#         result = data.fetchall()
#         receivedHeaders = [col[0] for col in data.description]
#         print(result)
#         print(result[0][1])
#         # assert result[0][1] == "Balls to the Wall"
#         # headers = ['AlbumId', 'Title', 'ArtistId']
#         # assert receivedHeaders == headers
#         assert len(result) > 0

#    finally:
#         data.close()
#         dataTables.close()

# =========================================================================
# using MYSQL connection
# pip install mysql-connector-python (do the installation in your terminal)
# import mysql.connector

# def test_mysql_connection():
#     conn = mysql.connector.connect(
#         host="your_mysql_host",      # e.g. remotemysql.com
#         user="your_username",
#         password="your_password",
#         database="your_database"
#     )

#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM Employee")

#     rows = cursor.fetchall()

#     for row in rows:
#         print(row)

#     cursor.close()
#     conn.close()

# =========================================================================
# using PostgreSQL connection

#  pip install psycopg2-binary
#     import psycopg2

# def test_postgres_connection():
#     conn = psycopg2.connect(
#         host="your_postgres_host",
#         port="5432",
#         database="your_database",
#         user="your_username",
#         password="your_password"
#     )

#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM employee")
#     rows = cursor.fetchall()

#     for row in rows:
#         print(row)

#     cursor.close()
#     conn.close()

# =========================================================================
# using Microsoft SQL Server connection
# pip install snowflake-connector-python
# import snowflake.connector

# def test_snowflake_connection():
#     conn = snowflake.connector.connect(
#         user="YOUR_USERNAME",
#         password="YOUR_PASSWORD",
#         account="YOUR_ACCOUNT",      # e.g. xy12345.ap-south-1
#         warehouse="COMPUTE_WH",
#         database="TEST_DB",
#         schema="PUBLIC",
#         role="SYSADMIN"
#     )

#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM EMPLOYEE")
#     rows = cursor.fetchall()

#     for row in rows:
#         print(row)

#     cursor.close()
#     conn.close()




