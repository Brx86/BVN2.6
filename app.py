from threading import Thread
from flask import Flask

app = Flask(__name__)


@app.route("/<path:path>")
def hello_world(path):
    return app.send_static_file(path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", threaded=True)
