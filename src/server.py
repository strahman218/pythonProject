from flask import Flask, render_template, request, redirect
from api import api

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("homepage.html")


@app.route("/search")
def search(error_messages=None, speed=None, location1=None, location2=None, results=None):
    if results is None:
        results = {}
        
    results.speed = speed
    results.location1 = location1
    results.location2 = location2
    return render_template("search.html", error_messages=error_messages, speed=speed, location1=location1, location2=location2, results=results)


@app.route("/getLocations", methods=['GET', 'POST'])
def get_locations():
    error_messages = []
    location1 = request.form['results.location1']
    location2 = request.form['results.location2']
    speed = "3.5" if request.form['results.speed'] is '' else request.form['speed']

    if request.form['location1'] == '':
        error_messages.append("Please enter a valid origin!")
    if request.form['location2'] == '':
        error_messages.append("Please enter a valid destination!")

    print("error messages: ")
    print(error_messages)
    if len(error_messages) > 0:
        print("there are some error messages!")
        results = {'location1': location1, 'location2': location2}
        return search(error_messages, speed, results)
    else:
        formatted_location1 = location1.replace(",", " ")
        formatted_location2 = location2.replace(",", " ")

        results = api.get_location_data(formatted_location1, formatted_location2, speed)
        return render_template("search.html", error_messages=error_messages, speed=speed, results=results)


if __name__ == "__main__":
    app.run(debug=True)
