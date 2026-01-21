import os
import csv
from bs4 import BeautifulSoup

input_path = "data/raw_data/web_data.html"
market_path = "data/processed_data/market_data.csv"
news_path = "data/processed_data/news_data.csv"

if not os.path.exists(input_path):
	print(f"Error: Couldn't find {input_path}")
	exit()

print(f"Reading {input_path}...")
with open(input_path, "r", encoding="utf-8") as file:
	soup = BeautifulSoup(file, "html.parser")

print("Filtering market banner fields...")
market_data = []
cards = soup.select('[class*="MarketCard-container"]')
for card in cards:
	symbol = card.select_one('[class*="MarketCard-symbol"]')
	stock_position = card.select_one('[class*="MarketCard-stockPosition"]')
	change_percentage = card.select_one('[class*="MarketCard-changesPct"]')

	if symbol and stock_position and change_percentage:
		market_data.append([symbol.get_text(strip=True), stock_position.get_text(strip=True), change_percentage.get_text(strip=True)])

print("Filtering latest news fields...")
news_data=[]
news = soup.select('[class*="LatestNews-item"]')
for new in news:
	timestamp = new.select_one('[class*="LatestNews-timestamp"]')
	link = new.select_one('a')

	if timestamp and link:
		news_time = timestamp.get_text(strip=True)
		news_link = link.get('href')

		if not news_link or "/pro/" in news_link or "/investingclub/" in news_link:
			continue

		news_title = link.get_text(strip=True)
		if not news_title:
			continue
	news_data.append([news_time, news_title, news_link])

print(f"Storing market banner data to {market_path}...")
with open(market_path,"w",newline="",encoding="utf-8") as f:
	writer=csv.writer(f)
	writer.writerow(["Symbol", "StockPosition", "ChangePct"])
	writer.writerows(market_data)

print(f"Storing new data to {news_path}...")
with open(news_path,"w",newline="",encoding="utf-8") as f:
	writer=csv.writer(f)
	writer.writerow(["Timestamp", "Title", "Link"])
	writer.writerows(news_data)

print(f"CSV files created!")
