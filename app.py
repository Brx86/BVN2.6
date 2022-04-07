from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def entry():
    return redirect("index.html")


@app.route("/<path:path>")
def ruffle(path):
    return app.send_static_file(path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
