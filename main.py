from flask import url_for, Flask, render_template, request
from werkzeug.utils import redirect
import main_db_client


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
@app.route("/main", methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        db = main_db_client.DB()
        tiles_data_list = db.view_records()
        return render_template("main.html", tiles_list=tiles_data_list, size=len(tiles_data_list))
    else:
        # DON'T TOUCH IT
        tile_id = request.form["caller"]
        return redirect(url_for('.info', tile_id=tile_id))


@app.route("/info", methods=['GET', 'POST'])
def info():
    # DON'T TOUCH IT
    db = main_db_client.DB()
    tile_id = request.args.get('tile_id', type=int)
    tile_data = db.get_record(tile_id)
    return render_template("info.html", tile_data=tile_data)


@app.route("/new_event", methods=['GET', 'POST'])
def new_event():
    if request.method == 'GET':
        return render_template("new_event.html")
    if request.method == 'POST':
        db = main_db_client.DB()
        name = request.form["name"]
        type = request.form["type_input"]
        about = request.form["about"]
        date = request.form["date_input"]
        time = request.form["time_input"]
        address = request.form["address_input"]
        price = request.form["price_input"]
        conditions = request.form["conditions_input"]
        is_open = request.form["visibility_input"]
        db.insert_data(name, type, date, time, price, address, "", is_open, about, conditions)
        return render_template("new_event.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
