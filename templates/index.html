import scrapy
from bs4 import BeautifulSoup
import requests
import sqlite3
import re
import openai
import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template, request

# ⚡ CONFIGURATION ⚡
DB_NAME = "entreprises.db"
openai.api_key = "TA_CLE_OPENAI"
SMTP_SERVER = "smtp.yourprovider.com"
SMTP_PORT = 587
SMTP_USER = "tonemail@example.com"
SMTP_PASS = "ton_mdp"

# 🕵️ SCRAPING - Récupérer les entreprises
class EntrepriseSpider(scrapy.Spider):
    name = "entreprises"
    start_urls = ["https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=artisan&ou=france"]

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        entreprises = soup.find_all("div", class_="bi-bloc")

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS entreprises 
                          (nom TEXT, email TEXT, secteur TEXT, site TEXT)''')

        for e in entreprises:
            nom = e.find("h2").text.strip()
            site = e.find("a")["href"] if e.find("a") else None
            email = self.get_email_from_site(site) if site else None
            secteur = "Artisanat"

            if email:
                cursor.execute("INSERT INTO entreprises (nom, email, secteur, site) VALUES (?, ?, ?, ?)", 
                               (nom, email, secteur, site))
                conn.commit()

        conn.close()

    def get_email_from_site(self, url):
        try:
            page = requests.get(url, timeout=5)
            emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", page.text))
            return list(emails)[0] if emails else None
        except:
            return None

# ✉️ GENERATION D'EMAIL AVEC GPT-4
def generate_email(nom, secteur):
    prompt = f"Écris un email professionnel pour proposer des services de cybersécurité à {nom}, spécialisé dans {secteur}."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Tu es expert en rédaction d’emails professionnels."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# 📤 ENVOI DES EMAILS
def send_email(to_email, subject, body):
    msg = MIMEText(body, "plain")
    msg["From"] = SMTP_USER
    msg["To"] = to_email
    msg["Subject"] = subject

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, to_email, msg.as_string())
            print(f"Email envoyé à {to_email}")
    except Exception as e:
        print(f"Erreur en envoyant à {to_email}: {e}")

# 🌐 INTERFACE FLASK
app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entreprises")
    entreprises = cursor.fetchall()
    conn.close()
    return render_template("index.html", entreprises=entreprises)

@app.route("/send_email", methods=["POST"])
def send_email_route():
    email = request.form["email"]
    nom = request.form["nom"]
    secteur = request.form["secteur"]
    email_text = generate_email(nom, secteur)
    send_email(email, "Sécurisez votre entreprise", email_text)
    return "Email envoyé avec succès !"

# 🚀 LANCER FLASK
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
