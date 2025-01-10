import sqlite3

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

try:
    cursor.execute("PRAGMA table_info(your_table_name)")

# Fetch all columns of the table
    columns = cursor.fetchall()

# Print the column details
    for column in columns:
            print(f"Column: {column[1]}, Type: {column[2]}")

finally:
    # Ensure the connection is closed, even if there's an error
    connection.close()