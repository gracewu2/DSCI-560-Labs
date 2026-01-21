# Lab 1: CNBC Market Data & News Scraper

## Overview
This lab is a web scraping pipeline designed to extract market data and the latest news headlines from the CNBC homepage through the Ubuntu Linux (VirtualBox VM) environment with libraries like 'Selenium', 'BeautifulSoup4', and 'Chromium Browser'.
Files consist of:
- 'scripts/task_1.py': Prints 'Hello, [name]!'.
- 'scripts/web_scraper.py': Launches a headless browser and saves the raw HTML.
- 'scripts/data_filter.py': Processes the raw HTML to extract specific Market and News data into CSV format.
- 'data/raw_data/': Contains the cached HTML source.
- 'data/processed_data/': Contains the final output, consisting of:
  - 'market_data.csv': Symbols, positions, and percentage changes.
  - 'news_data.csv': Timestamps, headlines, and direct links.
 
## How to Run in bash
1. Install Dependencies:

   sudo apt update && sudo apt install chromium-browser chromium-chromedriver -y
   pip install selenium beautifulsoup4

3. Run task 1, scraper, and filter to retrieve output:

   python3 scripts/task_1.py
   python3 scripts/web_scraper.py
   python3 scripts/data_filter.py
   
