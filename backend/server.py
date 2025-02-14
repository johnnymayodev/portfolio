from flask import Flask, render_template #type: ignore
import os

app = Flask(__name__, template_folder="../templates", static_folder="../static")
port = 3000


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/wip")
def wip():
    return render_template("wip.html")


if __name__ == "__main__":
    app.run(debug=True, port=port)
