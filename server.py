from flask import Flask, render_template

from challenges import register_blueprints

app = Flask(__name__)
register_blueprints(app)


@app.errorhandler(500)
def error(e):
    return "Invalid input", 400


@app.route('/')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run()
