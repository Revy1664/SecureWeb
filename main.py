import flask

# creating an app
app = flask.Flask(__name__)

# routes
@app.route("/")
def index():

	return "Hello!"


app.run(debug=True)