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

def insert_into_research_table(data: tuple) -> None:
    insert_query = """
    INSERT INTO watch_research_table (brand_name, model, price, link, box, papers, watch_creation_date, date_added)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    cursor.execute(insert_query, data)
    print("Data inserted successfully!")

def insert_into_sales_table(data: tuple) -> None:
    insert_query = """
    INSERT INTO watch_sales_table (brand_name, model, buy_price, sell_price, box, papers, watch_creation_date, buy_date, sold_date)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    cursor.execute(insert_query, data)
    print("Data inserted successfully!")

def read_from_research_table() -> list[tuple]:
    read_query = """
    SELECT * FROM watch_research_table;
    """
    cursor.execute(read_query)
    data = cursor.fetchall()
    return data

data = ('Rolex', 'Submariner', 7500.00, 'http://example.com/rolex-submariner', 1, 1, '2023-01-01', '2023-10-01')
insert_into_research_table(data)
print(len(read_from_research_table()))
conn.close()