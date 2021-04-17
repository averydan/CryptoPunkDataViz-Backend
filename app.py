from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
conn = psycopg2.connect("dbname=CryptoPunks user=postgres password=B9i18O69")
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


@app.route('/punk/<inpId>')
def punk(inpId):
    market_results = []
    cursor = conn.cursor()
    select_market_where_id = f"select * from market_df where id = {inpId}"
    cursor.execute(select_market_where_id)
    market_data = cursor.fetchall()
    select_punk_where_id = f"select * from punks_df where id = {inpId}"
    cursor.execute(select_punk_where_id)
    punk_data = cursor.fetchall()
    punk_result = {
    "ID": punk_data[0][0],
    "Type": punk_data[0][1],
    "Count": punk_data[0][2],
    "Accessories": punk_data[0][3]
    }
    for row in market_data:
        market_dict = {}
        market_dict["ID"] = row[2]
        market_dict["Date"] = row[0]
        market_dict["Time"] = row[1]
        market_dict["Price"] = row[3]
        market_results.append(market_dict)

    if market_results == []:
        market_results.append('No Market Data')

    final_result = {
        "Punk_Data": punk_result,
        "Market_Data": market_results
    }

    return jsonify(final_result)







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






@app.route('/markettopten')
def markettopten():
    cursor = conn.cursor()
    select_market_where_id = f"select * from market_df order by Price ETH desc limit 10"
    cursor.execute(select_market_where_id)
    market_data = cursor.fetchall()
    # select_punk_where_id = f"select * from punks_df where id = {inpId}"
    # cursor.execute(select_punk_where_id)
    # punk_data = cursor.fetchall()
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
    

@app.route('/count/<inpCount>')
def count(inpCount):
    cursor = conn.cursor()
    select_punk_where_count = f"select * from punks_df where count = {inpCount}"
    cursor.execute(select_punk_where_count)
    punk_data = cursor.fetchall()
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


