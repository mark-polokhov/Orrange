from flask import Flask, render_template, request
from main_db_client import WikiPlacesRecognition, PageNotFound


app = Flask(__name__)
wiki_places_recognition = WikiPlacesRecognition.from_api_token_path("mapbox_key.txt")


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/data", methods=["POST", "GET"])
def data():
    if request.method == "GET":
        return render_template("form.html")
    if request.method == "POST":
        try:
            wiki_places = wiki_places_recognition(request.form["wiki_page_url"])
        except PageNotFound:
            return render_template("form.html")
        api_key = wiki_places_recognition.get_api_key()
        form_data = {
            "wiki_page_url": request.form["wiki_page_url"],
            "wiki_places": wiki_places,
            "api_key": api_key,
        }
        return render_template("data.html", form_data=form_data)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=False)
