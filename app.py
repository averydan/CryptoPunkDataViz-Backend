from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2


app = Flask(__name__)
conn = psycopg2.connect("dbname=CryptoPunks user=postgres password=jerren")
cursor = conn.cursor()
select_all_market = "select * from market_df"
cursor.execute(select_all_market)
market_data = cursor.fetchall()
select_all_punks = "select * from punks_df"
cursor.execute(select_all_punks)
punk_data = cursor.fetchall()



@app.route('/')
def hello():
    return f"Use slash market to get up to date market data, and slash punks for punk listing."

@app.route('/market')
def market():
    market_results = []
    for row in market_data:
        market_dict = {}
        market_dict["ID"] = row[2]
        market_dict["Date"] = row[0]
        market_dict["Time"] = row[1]
        market_dict["Price"] = row[3]
        market_results.append(market_dict)

    return jsonify(market_results)


@app.route('/punks')
def punks():
    punk_results = []
    for row in punk_data:
        punk_dict = {}
        punk_dict["ID"] = row[0]
        punk_dict["Type"] = row[1]
        punk_dict["Count"] = row[2]
        punk_dict["Accessories"] = row[3]
        punk_results.append(punk_dict)

    return jsonify(punk_results)


if __name__ == '__main__':
    app.run(debug=True)