from flask import Flask

app = Flask(__name__)


@app.route('/user/<int:us_id>/')
def index(us_id):
    #return f"hello user {us_id}"
    return ""


app.run(debug=True)
