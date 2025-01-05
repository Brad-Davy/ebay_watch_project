from data_pulling.data_pulling import data_puller
from sql.database_IO import db_io
from datetime import datetime


db = db_io()


def convert_to_float(value: str) -> float:
    value = value.replace("£", "").replace("$", "")
    try:
        return float(value)
    except:
        return 0.0


def add_watches_to_research_table(query: str) -> None:
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


data = (
    "Tag Huer",
    "Formula 1",
    "Automatic",
    "Bought",
    570,
    "Yes",
    "No",
    "2021",
    "01-01-2025",
)
db.insert_into_sales_table(data)
