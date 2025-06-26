from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/resume")
def resume():
    return send_file("resume.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)


# this change to verify on server
