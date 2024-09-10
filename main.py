from flask import Flask, render_template

# creating an app
app = Flask(__name__)

# routes
@app.route("/")
def index_view():
    """
        The main page of the web application
    """
    return render_template("index.html")

@app.route("/about")
def about_view():
    """
        The page of detail information
    """

    return render_template("about.html")

@app.route("/contact")
def contact_view():
    """
        The page that contains contact info
    """

    return render_template("about.html")


app.run(debug=True)