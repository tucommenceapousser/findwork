from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect("entreprises.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entreprises")
    entreprises = cursor.fetchall()
    conn.close()
    return render_template("index.html", entreprises=entreprises)

@app.route("/send_email", methods=["POST"])
def send_email():
    email = request.form["email"]
    # Appeler send_email() ici
    return "Email envoyé avec succès !"

if __name__ == "__main__":
    app.run(debug=True)
