import requests
from bs4 import BeautifulSoup
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import shutil

url = "https://www.cnbc.com/world/?region=world"
output_file_path = "data/raw_data/web_data.html"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

chromium_browser = shutil.which("chromium-browser")
if chromium_browser:
	chrome_options.binary_location = chromium_browser
	print(f"Found browser: {chromium_browser}")
else:
	print("Error.")

print("Launching Selenium...")
try:
	service = Service("/usr/bin/chromedriver")
	driver = webdriver.Chrome(service=service, options=chrome_options)
	print(f"Retrieving {url}...")
	driver.get(url)

	driver.execute_script("window.scrollTo(0,500);")
	time.sleep(2)
	driver.execute_script("window.scrollTo(0,0);")
	time.sleep(10)

	html = driver.page_source
	driver.quit()

	soup = BeautifulSoup(html, 'html.parser')
	with open(output_file_path, "w", encoding="utf-8") as file:
		file.write(soup.prettify())

	print(f"Data saved to {output_file_path}")

except Exception as e:
	print(f"An error occurred: {e}")
	try: driver.quit()
	except: pass


