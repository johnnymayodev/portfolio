from flask import Flask, render_template #type: ignore


app = Flask(__name__, template_folder="../templates", static_folder="../static")
port = 3000


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/wip")
def wip():
    return render_template("wip.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True, port=port)
