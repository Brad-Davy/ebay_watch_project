import pymssql


server = 'localhost'  
port = 1433  
database = 'master'  
username = 'sa' 
password = 'GreenHorses?!'  

try:
    conn = pymssql.connect(server=server, port=port, user=username, password=password, database=database)
    conn.autocommit(True)
    cursor = conn.cursor()
    print("Connection successful!")

except Exception as e:
    print("Error:", e)

create_research_table_query = """
    CREATE TABLE watch_research_table (
        brand_name NVARCHAR(50),
        model NVARCHAR(50),
        price DECIMAL(10, 2),
        link NVARCHAR(300),
        box BIT,
        papers BIT,
        watch_creation_date DATE,
        date_added DATE    );
"""

create_sales_table_query = """
    CREATE TABLE watch_sales_table (
        brand_name NVARCHAR(50),
        model NVARCHAR(50),
        buy_price DECIMAL(10, 2),
        sell_price DECIMAL(10, 2),
        box BIT,
        papers BIT,
        watch_creation_date DATE,
        buy_date DATE,
        sold_date DATE
                );
"""

cursor.execute('DROP TABLE watch_research_table;')
cursor.execute('DROP TABLE watch_sales_table;')
cursor.execute(create_research_table_query)
cursor.execute(create_sales_table_query)
conn.close()