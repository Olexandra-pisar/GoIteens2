from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "This is a main pages/activate"


if __name__ == "__main__":
    app.run()

























