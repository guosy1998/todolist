import psycopg2

conn = psycopg2.connect(database="todolist", user="tdluser", password="19980121", host="localhost", port="5432")

print("Opened database successfully")
