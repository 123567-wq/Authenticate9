import requests

def test_search_product_amazon():
    response = requests.get('https://amazon.com/search', params={'query': 'Titan watch'})
    assert response.status_code == 200
    data = response.json()
    assert 'products' in data

def test_search_product_flipkart():
    response = requests.get('https://flipkart.com/search', params={'query': 'Titan watch'})
    assert response.status_code == 200
    data = response.json()
    assert 'products' in data
