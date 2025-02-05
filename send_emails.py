import smtplib
import sqlite3
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.yourprovider.com"
SMTP_PORT = 587
SMTP_USER = "tonemail@example.com"
SMTP_PASS = "ton_mdp"

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

# Récupération des emails
conn = sqlite3.connect("entreprises.db")
cursor = conn.cursor()
cursor.execute("SELECT email, nom FROM entreprises")

for email, nom in cursor.fetchall():
    email_text = f"Bonjour {nom},\n\nNous pouvons vous aider à sécuriser votre activité...\n"
    send_email(email, "Sécurisez votre entreprise", email_text)

conn.close()
