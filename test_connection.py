# -*- coding: utf-8 -*-
import pypyodbc

connection = pypyodbc.connect(driver='{ODBC Driver 17 for SQL Server}',
                              server='tcp:databaseproject777.database.windows.net,1433',
                              database='test_database',
                              uid='Marcin',
                              pwd='projekt.BD2.1')

cursor = connection.cursor()
tables_and_columns = cursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS")

print("YOU SHOULD SEE ALL TABLES AND COLUMNS LISTED BELOW:\n")
for row in tables_and_columns:
    print(f"Table: {row[2]}; Column: {row[3]}")
