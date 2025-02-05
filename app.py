import scrapy
from bs4 import BeautifulSoup
import requests
import sqlite3

DB_NAME = "entreprises.db"

class EntrepriseSpider(scrapy.Spider):
    name = "entreprises"
    start_urls = [
        "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=artisan&ou=france"
    ]

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
        """Essaie d'extraire un email d'un site web"""
        try:
            page = requests.get(url, timeout=5)
            emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", page.text))
            return list(emails)[0] if emails else None
        except:
            return None
