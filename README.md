🛡️ Scraper & Mailer - Prospection Automatisée en Cybersécurité

Ce projet permet de trouver des entreprises émergentes (artisans, startups, inventeurs...), analyser leurs besoins, et leur envoyer automatiquement un email personnalisé via GPT-4 et SMTP.


---

🚀 Fonctionnalités

✅ Scraping des entreprises sur PagesJaunes (BeautifulSoup, Scrapy)
✅ Stockage en base de données (SQLite)
✅ Génération d’emails personnalisés avec GPT-4
✅ Envoi d’emails via SMTP sécurisé
✅ Interface web Flask pour gérer les contacts
✅ Automatisation complète avec un script Bash


---

📦 Installation

1️⃣ Prérequis

Python 3.8+

Pip3

Un compte OpenAI API (GPT-4)

Un serveur SMTP (Mailgun, SendGrid, Gmail, etc.)


2️⃣ Cloner le projet

```bash
git clone https://github.com/tonrepo/scraper-mailer.git
cd scraper-mailer
```

3️⃣ Configurer les variables

Dans main.py, remplace :

```python
openai.api_key = "TA_CLE_OPENAI"
SMTP_SERVER = "smtp.tonfournisseur.com"
SMTP_PORT = 587
SMTP_USER = "tonemail@example.com"
SMTP_PASS = "ton_mdp"
```

---

💻 Utilisation

Méthode 1️⃣ : Exécution manuelle

```bash
pip3 install -r requirements.txt
python3 main.py
```

Accède à l’interface web : http://127.0.0.1:5000/


---

Méthode 2️⃣ : Tout automatiser (script Bash)

```bash
chmod +x run.sh
./run.sh
```

✔ Installe les dépendances
✔ Lance le scraping
✔ Démarre Flask en arrière-plan
✔ Ouvre l’interface web automatiquement


---

📌 Interface Web

L’interface permet de :

Voir les entreprises trouvées

Envoyer un email en 1 clic

Suivre les envois et réponses



---

📜 Licence

Projet Open-Source sous licence MIT


---

💡 Améliorations futures

📊 Suivi des emails ouverts / répondus

🤖 Ajout d’une IA pour détecter les besoins précis des entreprises

📌 Scraping d’autres sources pour plus d’entreprises


