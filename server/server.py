from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates", static_folder="../static")
port = 55055


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=port)
