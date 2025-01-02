import pymssql


server = 'localhost'  
port = 1433  
database = 'master'  
username = 'sa' 
password = 'GreenHorses?!'  

try:
    conn = pymssql.connect(server=server, port=port, user=username, password=password, database=database)
    conn.autocommit(True)
    print("Connection successful!")

    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE watch_research_table;")

    conn.close()

except Exception as e:
    print("Error:", e)
