import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def test_flipkart_search_api(query, access_key):
    url = "https://flipkart.com/search"  # Replace with actual Flipkart API endpoint
    params = {'query': query, 'api_key': access_key}
    try:
        response = requests.get(url, params=params)
        logging.info(f"Flipkart Search Response Status Code: {response.status_code}")
        if response.status_code == 200:
            logging.info(f"Flipkart Search Response Content: {response.text}")
            try:
                data = response.json()  # Convert response to JSON
                logging.info(f"Flipkart Search Response Data: {data}")
                return data
            except ValueError as e:
                logging.error(f"Error parsing JSON: {e}")
                return None
        else:
            logging.error(f"Flipkart API request failed with status code {response.status_code}")
            return None
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return None

def fetch_flipkart_product_details(product_id, access_key):
    url = f"https://flipkart.com/product/{product_id}"  # Replace with actual endpoint
    headers = {
        'Authorization': f'Bearer {access_key}'
    }
    try:
        response = requests.get(url, headers=headers)
        logging.info(f"Flipkart Product Details Response Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            logging.info(f"Flipkart Product Details Data: {data}")
            return data
        else:
            logging.error(f"Flipkart API request failed with status code {response.status_code}")
            return None
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return None

# Example usage
flipkart_data = test_flipkart_search_api('Titan watch', 'your_flipkart_access_key')
if flipkart_data:
    validate_response_structure(flipkart_data.get('products', []))
    flipkart_product_id = flipkart_data.get('products', [])[0].get('product_id') if flipkart_data.get('products', []) else None
    if flipkart_product_id:
        flipkart_product_details = fetch_flipkart_product_details(flipkart_product_id, 'your_flipkart_access_key')
        print("Flipkart Product Details:", flipkart_product_details)
