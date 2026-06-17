from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "e496c20c02fd4bf0a5341129261706"

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

        response = requests.get(url)
        data = response.json()

        weather = {
            "city": data["location"]["name"],
            "temp": data["current"]["temp_c"],
            "humidity": data["current"]["humidity"],
            "condition": data["current"]["condition"]["text"]
        }

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)