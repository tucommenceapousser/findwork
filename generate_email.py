import openai
import sqlite3
import os

openai.api_key = "TA_CLE_OPENAI"

def generate_email(nom, secteur):
    prompt = f"""
    Écris un email professionnel pour proposer des services de cybersécurité à une entreprise nommée {nom}, spécialisée dans {secteur}.
    L'email doit être clair, professionnel et concis.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Tu es un expert en rédaction d’emails professionnels."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Générer un email pour chaque entreprise de la BDD
conn = sqlite3.connect("entreprises.db")
cursor = conn.cursor()
cursor.execute("SELECT nom, email, secteur FROM entreprises")

emails = []
for nom, email, secteur in cursor.fetchall():
    email_text = generate_email(nom, secteur)
    emails.append((nom, email, email_text))

conn.close()

# Sauvegarder les emails générés
with open("emails.txt", "w") as f:
    for nom, email, email_text in emails:
        f.write(f"To: {email}\nSubject: Sécurisez votre entreprise\n\n{email_text}\n\n---\n")
