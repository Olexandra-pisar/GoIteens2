import os
from flask import Flask, render_template, request, send_file
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
# from enums import MAX_SCORE, NAME, students


load_dotenv()

app = Flask(__name__)


# @app.route("/")
# def main():
#     return render_template("index.html")

@app.route("/base")
def base():
    return render_template("base.html", title="Python course")
#
# @app.route("/context")
# def context():
#     context_dict = {
#         "title": "Python Course",
#         "name": NAME,
#         "max_score": MAX_SCORE,
#         "students": students
#     }
#     return render_template("context.html", **context_dict)
#
#
# @app.route("/login", methods=["GET", "POST"])
# def login_user():
#     if request.method == "POST":
#         user = request.form.get("name")
#         return "Method POST"
#     else:
#         user = request.args.get("name")
#         return f'Method GET, user is {user}'




if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))

























