import requests
import sqlite3
from bs4 import BeautifulSoup

response = requests.get("https://www.bbc.com/ukrainian/features-66330880")
if response.status_code == 200:
    bs4 = BeautifulSoup(response.text, "html.parser")
    headlines = bs4.find_all("h2", class_="bbc-1aaitma eglt09e0")
    connection = sqlite3.connect("sqlite.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS first_table (place INTEGER PRIMARY KEY,name TEXT)")
    for i, headline in enumerate(headlines[:10]):
        cursor.execute("INSERT INTO first_table (place, name) VALUES (?, ?)", (i + 1, headline.text))
    connection.commit()
    connection.close()