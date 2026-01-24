# DSCI 560 Lab 2: Multi-Source Culinary Data Exploration

## Team Members:
Arya Miryala | USC ID:

Grace Wu | USC ID: 1980098805

Hui Xie | USC ID: 7956658480


## Overview
This lab extracts and cleans data from three different sources (CSV, HTML, PDF) to build a high-integrity dataset for an "Intelligent Culinary & Nutrition Assistant". By cleaning noisy raw data, we improve the correctness of AI responses through prioritizing food safety, modern relevance, and computational efficiency.

Files consist of:
- `data_exploration.py`: Main execution script to clean and transform the raw datasets.
- `recipes_cleaned.csv`: Cleaned structured data.
- `scraped_recipe_content.txt`: Cleaned web data.
- `historical_recipes_ocr.txt`: Cleaned PDF/OCR data.

## Installation & Dependencies
To run this script, you need Python 3.12+ and the following libraries:
- `pandas`: For CSV data manipulation.
- `requests` & `beautifulsoup4`: For web scraping.
- `pdfplumber` & `pytesseract`: For PDF and OCR text extraction.

Install Tesseract OCR:
- Mac: `brew install tesseract`

## Data Sources
- **GitHub CSV:** 1,000+ records, reduced from 60 columns to 3 for noise reduction.
- **Web HTML:** Scraped trending dish titles to provide real-time relevance.
- **PDF/OCR:** Extracted nutritional and safety data from institutional cookbooks.
