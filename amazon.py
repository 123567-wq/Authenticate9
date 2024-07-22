import requests
import logging
from bs4 import BeautifulSoup
from urllib.parse import quote
import time

# Configure logging
logging.basicConfig(level=logging.INFO)

def test_amazon_search_api(query, retries=3, delay=5):
    url = f"https://amazon.in/s?k={quote(query)}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, headers=headers)
            logging.info(f"Amazon Search Response Status Code: {response.status_code}")
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                products = []
                for item in soup.select('.s-main-slot .s-result-item'):
                    title = item.select_one('h2 a span')
                    price_whole = item.select_one('.a-price-whole')
                    price_fraction = item.select_one('.a-price-fraction')
                    product_id = item.get('data-asin')
                    if title and price_whole and price_fraction and product_id:
                        product = {
                            'product_id': product_id,
                            'name': title.get_text(strip=True),
                            'price': f"{price_whole.get_text(strip=True)}.{price_fraction.get_text(strip=True)}"
                        }
                        products.append(product)
                logging.info(f"Amazon Search Response Data: {products}")
                return products
            else:
                logging.error(f"Amazon request failed with status code {response.status_code}")
                if response.status_code == 503:
                    attempt += 1
                    logging.info(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                else:
                    return None
        except requests.RequestException as e:
            logging.error(f"An error occurred: {e}")
            return None
    logging.error("Maximum retries exceeded.")
    return None

# Example usage
amazon_data = test_amazon_search_api('Titan watch')
