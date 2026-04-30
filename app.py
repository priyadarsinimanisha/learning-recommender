from flask import Flask, render_template, request
from model.recommender import recommend

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    print("Route is working")  # 👈 add this
    results = []

    if request.method == "POST":
        subject = request.form.get("subject")
        level = request.form.get("level")
        results = recommend(subject, level)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run()