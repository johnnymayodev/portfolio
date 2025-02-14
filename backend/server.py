from flask import Flask, render_template #type: ignore
import os

app = Flask(__name__, template_folder="../templates", static_folder="../static")
port = 3000


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<path>")
def page(path):
    if path.endswith(".html"):
            path = path[:-5]  # Remove the last 5 characters (.html)

    if not os.path.exists(f"templates/{path}.html"):
        return render_template("404.html"), 404

    return render_template(path + ".html")


if __name__ == "__main__":
    app.run(debug=True, port=port)
