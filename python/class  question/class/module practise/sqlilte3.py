import sqlite3
connection = sqlite3.connect("databaseok.db")
cursor = connection.cursor()
# cursor.execute("""
# CREATE TABLE Student(
# S_no INTEGER,
# Student_name text,
# marks INTEGER
# )
# """)
# connection.commit()
# cursor.execute("""
# INSERT INTO Student values(
#     1,"ajay",85
# )
# """)
# connection.commit()
# cursor.execute("""
# INSERT INTO Student values(
#     2,"krishna",95
# )
# """)
# connection.commit()
cursor.execute("""
SELECT * FROM Student

""")
connection.commit()
result=cursor.fetchall()#fetchall fetchmany
print(result)