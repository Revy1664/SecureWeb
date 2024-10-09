import mysql.connector
from flask import Flask, render_template, request
from config import db_config
from user_agents import parse

# creating an app
app = Flask(__name__)

# connect to database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# routes
@app.route("/", methods=["GET",])
def index_view():
    """
        The main page of the web application
    """

    user_agent = request.headers.get("User-Agent")
    user_agent = parse(user_agent)
    browser = user_agent.browser.family

    _SQL = """insert into logs (browser, ip)
              values
              (%s, %s);
        """
    cursor.execute(_SQL, (browser, request.remote_addr))
    conn.commit()

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

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)