### **Web Scraper Code (Filename: `web_scraper.py`)**

import requests
from bs4 import BeautifulSoup
import csv

# Target website URL
URL = "https://example.com"

# Headers to mimic a real browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def fetch_data(url):
    """Fetch HTML content from the website."""
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve data. Status Code: {response.status_code}")
        return None

def parse_data(html):
    """Parse HTML and extract required information."""
    soup = BeautifulSoup(html, "html.parser")
    
    # Modify based on the website's structure
    data_list = []
    for item in soup.find_all("div", class_="data-class"):
        title = item.find("h2").text.strip()
        price = item.find("span", class_="price").text.strip()
        link = item.find("a")["href"]
        
        data_list.append([title, price, link])

    return data_list

def save_to_csv(data, filename="output.csv"):
    """Save extracted data to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Link"])
        writer.writerows(data)
    print(f"✅ Data saved to {filename}")

if __name__ == "__main__":
    html_content = fetch_data(URL)
    if html_content:
        scraped_data = parse_data(html_content)
        save_to_csv(scraped_data)
