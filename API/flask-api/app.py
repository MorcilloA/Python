from logging import log
from flask import Flask, request, jsonify
from flask.helpers import url_for
from flask.json.tag import JSONTag

app = Flask(__name__)

books = [
    {
        'id': 1,
        'titre': 'un titre',
    },
    {
        'id': 2,
        'titre': 'un autre titre random',
    }
]


@app.route("/")
def index():
    return "Hello my app"


@app.route("/api/books")
def listBooks():
    return jsonify(books)


# @app.route("/books/<id>")
# def detailById(id):
#     return jsonify(list(filter(lambda x: x["id"] == int(id), books)))

@app.route("/books/<title>")
def detailByTitle(title):
    return jsonify(list(filter(lambda x: x["titre"] == str(title), books)))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Do the login"

    else:
        return "Show the login form"


@app.route("/about")
def about():
    return "The about page"


@app.route("/urls")
def urls():
    return "{}".format(url_for("about"))


def get_a_response():
    return "Hello"


if __name__ == '__main__':
    app.run(debug=True)
