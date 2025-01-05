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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)
