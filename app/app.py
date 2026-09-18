from flask import Flask, render_template, request
from data.experiences import experiences
from data.formations import formations


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/experiences")
def experiences_page():
    return render_template("experiences.html", experiences=experiences)

@app.route("/formations")
def formations_page():
    return render_template("formations.html", formations=formations)

@app.route("/projects")
def projects():
    return render_template("projets.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        print(name)
        print(email)
        print(message)

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)