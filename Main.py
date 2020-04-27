from flask import *
import sqlite3
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("view.html")


@app.route("/view", methods=["POST"])
def view():
    global tables
    tables = []
    global Database
    Database = request.form["db"]
    con = sqlite3.connect(Database)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table = cur.fetchall()
    for Alltable in table:
        for i in range(len(Alltable)):
            tables.append(Alltable[i])

    return render_template("View.html", tables=tables, Database=Database)


@app.route("/viewTable", methods=["POST"])
def saveDetails():
    column = []
    global tablename
    global df
    tablename = request.form["tab"]
    con = sqlite3.connect(Database)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    query="select * from {0}".format(tablename)
    cur.execute(query)
    rows = cur.fetchall()
    colnames = cur.description
    for Allcolumns in colnames:
        column.append(Allcolumns[0])

    columnlength = len(column)

    CompleteDet = []
    for Allrow in rows:
        Details = []
        for k in range(0, columnlength):
            Details.append(Allrow[k])
        CompleteDet.append(Details)
	
    df=pd.DataFrame(list(rows),columns=column)
    df.to_csv("output.csv")

    return render_template("view.html", tables=tables, Database=Database, column=column, rows=rows, columnlength=columnlength, CompleteDet=CompleteDet, tablename=tablename)

@app.route('/return-files/')
def return_files_tut():
	try:
		return send_file('output.csv', attachment_filename='output.csv')
	except Exception as e:
		return str(e)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9090)
