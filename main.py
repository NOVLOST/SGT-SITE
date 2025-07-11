from flask import Flask,render_template, url_for,request

app = Flask(__name__)

data_table = [["артур","4522","0102"],["альберт","5459","1204"],["александр","4151","0707"]]

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html",table_info=data_table)

@app.route("/index",methods=["POST"])
@app.route("/",methods=["POST"])
def index_POST():
    dev_name = request.form["names"]
    part_name = request.form["part"]
    date = request.form["date"]
    data_table.append([

        dev_name,
        part_name,
        date
    ])

    return render_template("index.html",table_info = data_table)


if __name__ == "__main__":
    app.run(debug=True)