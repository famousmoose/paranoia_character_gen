from flask import Flask, render_template
from paranoialib.character import Character

app = Flask(__name__)

@app.route("/")
def root_page():
    character = Character()
    return render_template('index.html',character=character)


if __name__ == '__main__':
    app.run(debug=True)