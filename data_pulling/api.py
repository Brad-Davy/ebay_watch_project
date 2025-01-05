import flask
from flask import jsonify
from data_pulling import data_puller
from sql.database_IO import db_io

app = flask.Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/current_listings/<query>")
def current_listings(query: str) -> dict:
    data_puller_instance = data_puller(query)
    data_puller_instance.search_current_listings()
    return str(data_puller_instance.current_search_df)


@app.route("/completed_listings/<query>")
def completed_listings(query):
    data_puller_instance = data_puller(query)
    data_puller_instance.search_completed_listings()
    return str(data_puller_instance.completed_search_df)


@app.route("/api/sales")
def get_sales():
    db = db_io()
    data = db.execute_query("SELECT * FROM watch_sales_table")
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=2000)
