from data_pulling.data_pulling import data_puller
from sql.database_IO import db_io
from datetime import datetime


dpuller = data_puller("Tag Heuer Formula 1")
db = db_io()

dpuller.search_completed_listings()

number_of_collumns = len(dpuller.completed_search_df["title"])
todays_date = datetime.today().strftime("%Y-%m-%d")


def convert_to_float(value: str) -> float:
    value = value.replace("£", "").replace("$", "")
    try:
        return float(value)
    except:
        return 0.0


def add_watches(query: str) -> None:
    for i in range(number_of_collumns):
        db.insert_into_research_table(
            (
                dpuller.completed_search_df["title"][i],
                convert_to_float(dpuller.completed_search_df["price"][i]),
                dpuller.completed_search_df["link"][i],
                dpuller.completed_search_df["box"][i],
                dpuller.completed_search_df["papers"][i],
                todays_date,
                todays_date,
                dpuller.completed_search_df["movement"][i],
            )
        )


prices = db.execute_query("SELECT price FROM watch_research_table;")
print(float(prices[0][0]))
