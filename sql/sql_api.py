import flask
from flask import jsonify
from database_IO import db_io
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/api/sales")
def get_sales():
    db = db_io()
    data = db.execute_query("SELECT * FROM watch_sales_table")
    return jsonify(data)


@app.route(
    "/api/sales_insert/<brand_name>/<model>/<movement>/<action>/<price>/<box>/<papers>/<watch_creation_date>/<action_date>"
)
def insert_into_sales(
    brand_name: str,
    model: str,
    movement: str,
    action: str,
    price: str,
    box: str,
    papers: str,
    watch_creation_date: str,
    action_date: str,
):
    db = db_io()
    data = (
        brand_name,
        model,
        movement,
        action,
        float(price),
        box,
        papers,
        watch_creation_date,
        action_date,
    )
    db.insert_into_sales_table(data)
    return "Data inserted successfully!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)
