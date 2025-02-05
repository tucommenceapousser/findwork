#!/bin/bash

echo "🚀 Initialisation du projet..."
sleep 1

# 📌 Vérifier si Python et pip sont installés
if ! command -v python3 &>/dev/null; then
    echo "❌ Python3 n'est pas installé. Installe-le avant de continuer."
    exit 1
fi

if ! command -v pip3 &>/dev/null; then
    echo "❌ Pip3 n'est pas installé. Installe-le avant de continuer."
    exit 1
fi

# 📌 Installer les dépendances si elles ne sont pas encore installées
echo "📦 Installation des dépendances..."
pip3 install --upgrade pip
pip3 install scrapy beautifulsoup4 requests openai smtplib flask sqlite3 &>/dev/null

# 📌 Vérifier si la base de données SQLite existe
DB_NAME="entreprises.db"
if [ ! -f "$DB_NAME" ]; then
    echo "📂 Création de la base de données SQLite..."
    touch "$DB_NAME"
fi

# 📌 Lancer le scraping
echo "🕵️ Lancement du scraping des entreprises..."
python3 -c "import main; EntrepriseSpider().parse(requests.get('https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=artisan&ou=france'))"

# 📌 Lancer le serveur Flask en arrière-plan
echo "🌐 Démarrage du serveur Flask..."
nohup python3 main.py &>/dev/null &

# 📌 Attendre 2 secondes pour s'assurer que Flask démarre
sleep 2

# 📌 Ouvrir l'interface web dans le navigateur
echo "🖥️ Interface disponible sur : http://ip:port/"
xdg-open "http://127.0.0.1:5000/" 2>/dev/null || open "http://127.0.0.1:5000/" 2>/dev/null

echo "✅ Tout est prêt !"
