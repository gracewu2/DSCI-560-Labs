import pandas as pd
import requests
from bs4 import BeautifulSoup
import pdfplumber
import pytesseract
from pdf2image import convert_from_bytes
import io
import os


# CSV
def get_recipes_csv():
    print("Loading Recipes in CSV...")
    csv_url = "https://raw.githubusercontent.com/cweber/cookbook/master/recipes.csv"
    
    # Load the dataset
    df = pd.read_csv(csv_url, engine='python', on_bad_lines='skip')
    
    # Print first few records
    print("\nColumn Names:")
    print(df.columns.tolist()) 
    print("\nFirst 3 Original Records:")
    pd.set_option('display.max_columns', None) 
    pd.set_option('display.width', 1000)
    print(df.head(3))

    # Dimensions and size
    print(f"Dimensions (Rows, Columns): {df.shape}")
    print(f"Total Size (Data Points): {df.size}")
    print(f"Missing Values identified: {df.isnull().sum().sum()}")
    
    # Clean by keeping only the title, category, and directions
    df_clean = df[['Title', 'Category', 'Directions']].dropna()
    
    # Save the cleaned version
    df_clean.to_csv("recipes_cleaned.csv", index=False)
    print("Saved: recipes_cleaned.csv")


# HTML
def get_recipes_html():
    print("\nLoading Trending Recipes via HTML...")
    url = "https://www.allrecipes.com/recipes/80/main-dish/"
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        # Get HTML content from the website
        response = requests.get(url, headers=headers, timeout=10)

        print("\nPreview of Original HTML Source of the first 500 characters:")
        print(response.text[:500])

        # Use BeautifulSoup to parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all titles to show a broad range of data
        recipe_links = soup.find_all('span', class_='card__title-text')
        # Store titles in a clean list
        titles = [link.get_text().strip() for link in recipe_links]
        
        if titles:
            print(f"Collected {len(titles)} general recipes.")
            # Sample after cleaning
            print(f"Sample of first 3 titles: {titles[:3]}") 
            
            # Save scraped list to a text file
            with open("scraped_recipe_content.txt", "w", encoding="utf-8") as f:
                f.write("General Trending Recipes:\n" + "="*25 + "\n")
                f.write("\n".join(titles))
            print("Saved: scraped_recipe_content.txt")
        else:
            print("No titles found.")
                
    except Exception as e:
        print(f"Scraping Error: {e}")


# PDF
def get_cookbook_pdf():
    print("\nLoading cookbook PDF…")
    pdf_url = "https://foodhero.org/sites/foodhero-prod/files/health-tools/cookbook.pdf"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(pdf_url, headers=headers, timeout=20)
        
        # Sample of original data 
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        print(f"Preview of original PDF file (First 100 bytes): {response.content[:100]}")

        # Verify it is actually a PDF before processing
        if not response.content.startswith(b'%PDF'):
            print(f"Error: Expected PDF but got {response.headers.get('Content-Type')}")
            return

        # Extract text using a PDF-to-text library
        with pdfplumber.open(io.BytesIO(response.content)) as pdf:
            # Extracting from page 5 (contains recipe tools and titles)
            page = pdf.pages[4] 
            text = page.extract_text()
        
        # Handle documents that require OCR
        if not text or len(text.strip()) < 50:
            print("Standard extraction failed. Running OCR...")
            images = convert_from_bytes(response.content, first_page=5, last_page=5)
            text = pytesseract.image_to_string(images[0])
            
        print(f"Extracted Sample of Cleaned Data: {text[:150].strip()}...")
        
        # Save to a text file as part of the clean dataset
        with open("historical_recipes_ocr.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Saved historical_recipes_ocr.txt")
        
    except Exception as e:
        print(f"PDF Error: {e}")
    

if __name__ == "__main__":
    get_recipes_csv()
    get_recipes_html()
    get_cookbook_pdf()

