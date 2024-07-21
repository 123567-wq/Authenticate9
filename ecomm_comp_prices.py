def compare_prices(amazon_price, flipkart_price):
    if amazon_price < flipkart_price:
        return 'Amazon has the lower price'
    elif flipkart_price < amazon_price:
        return 'Flipkart has the lower price'
    else:
        return 'Both platforms have the same price'
