import pymssql


class db_io:
    def __init__(self):
        self.server = "localhost"
        self.port = 1433
        self.database = "master"
        self.username = "sa"
        self.password = "GreenHorses?!"

    def _connect_to_database(self):
        try:
            conn = pymssql.connect(
                server=self.server,
                port=self.port,
                user=self.username,
                password=self.password,
                database=self.database,
            )
            conn.autocommit(True)
            print("Connection successful!")
            return conn

        except Exception as e:
            print("Error:", e)

    def insert_into_research_table(self, data: tuple) -> None:
        conn = self._connect_to_database()
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO watch_research_table (title, price, link, box, papers, watch_creation_date, date_added, movement)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, data)
        conn.close()
        print("Data inserted successfully!")

    def insert_into_sales_table(self, data: tuple) -> None:
        conn = self._connect_to_database()
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO watch_sales_table (brand_name, model, movement, action, price, box, papers, watch_creation_date, action_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, data)
        conn.close()
        print("Data inserted successfully!")

    def read_from_research_table(self) -> list[tuple]:
        conn = self._connect_to_database()
        cursor = conn.cursor()
        read_query = """
        SELECT * FROM watch_research_table;
        """
        cursor.execute(read_query)
        data = cursor.fetchall()
        conn.close()
        print(f"Read {len(data)} rows read from the database.")
        return data

    def read_from_sales_table(self) -> list[tuple]:
        conn = self._connect_to_database()
        cursor = conn.cursor()
        read_query = """
        SELECT * FROM watch_sales_table;
        """
        cursor.execute(read_query)
        data = cursor.fetchall()
        conn.close()
        print(f"Read {len(data)} rows read from the database.")
        return data

    def execute_query(self, query: str) -> list[tuple]:
        conn = self._connect_to_database()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        print(f"Read {len(data)} rows read from the database.")
        return data


if __name__ == "__main__":
    db = db_io()
    db.read_from_research_table()
    db.read_from_sales_table()
