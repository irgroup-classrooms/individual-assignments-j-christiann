import re 


def main():
    
import re
from collections import Counter

# Function to extract order numbers
def extract_order_numbers(text):
    # Adjust the pattern if needed
    pattern = r'\b[A-Za-z0-9\-]+\b'  # Order numbers can be alphanumeric
    return re.findall(pattern, text)

# Function to extract product names (assuming words with more than 2 characters)
def extract_product_names(text):
    # Adjust pattern to match product names; this assumes they are capitalized words
    pattern = r'\b[A-Za-z]{3,}\b'
    return re.findall(pattern, text)

# Function to extract prices
def extract_prices(text):
    # Price pattern: matches numbers with optional decimal points and two digits
    pattern = r'\$\d+\.\d{2}'
    return re.findall(pattern, text)

# Function to extract order dates (assuming dates are in YYYY-MM-DD format)
def extract_order_dates(text):
    # Date pattern: matches YYYY-MM-DD format
    pattern = r'\d{4}-\d{2}-\d{2}'
    return re.findall(pattern, text)

# Function to change date format to DD/MM/YYYY
def change_date_format(date):
    # Change from YYYY-MM-DD to DD/MM/YYYY
    return re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', date)

# Function to extract orders with prices greater than $500
def extract_orders_over_500(prices, orders, products):
    return [orders[i] for i in range(len(prices)) if float(prices[i][1:]) > 500]

# Function to count product occurrences
def count_product_occurrences(products):
    return Counter(products)

# Function to find products priced over $500
def extract_orders_ending_in_99(prices, orders):
    return [orders[i] for i in range(len(prices)) if prices[i].endswith('.99')]

# Function to find the cheapest product
def find_cheapest_product(prices, products):
    # Convert prices to float and find the product with the lowest price
    price_float = [float(price[1:]) for price in prices]
    min_price_idx = price_float.index(min(price_float))
    return products[min_price_idx], prices[min_price_idx]

# Main function to parse the file and perform the required tasks
def parse_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Extract data
    order_numbers = extract_order_numbers(text)
    product_names = extract_product_names(text)
    prices = extract_prices(text)
    order_dates = extract_order_dates(text)

    # Extract orders for products priced over $500
    orders_over_500 = extract_orders_over_500(prices, order_numbers, product_names)

    # Change the date format to DD/MM/YYYY
    formatted_dates = [change_date_format(date) for date in order_dates]

    # Extract product names that have more than 6 characters
    long_product_names = [product for product in product_names if len(product) > 6]

    # Count the occurrence of each product
    product_count = count_product_occurrences(product_names)

    # Extract orders with prices ending in .99
    orders_ending_in_99 = extract_orders_ending_in_99(prices, order_numbers)

    # Find the cheapest product
    cheapest_product, cheapest_price = find_cheapest_product(prices, product_names)

    # Print results
    print("Extracted Order Numbers:", order_numbers)
    print("Extracted Product Names:", product_names)
    print("Extracted Prices:", prices)
    print("Extracted Order Dates:", order_dates)
    print("Orders for Products Priced Over $500:", orders_over_500)
    print("Formatted Order Dates (DD/MM/YYYY):", formatted_dates)
    print("Product Names with More Than 6 Characters:", long_product_names)
    print("Product Count:", product_count)
    print("Orders with Prices Ending in .99:", orders_ending_in_99)
    print(f"Cheapest Product: {cheapest_product} at {cheapest_price}")

# Run the script (change the file path to your actual file path)
parse_file('csv/orders.csv')


if __name__ == '__main__':
    main()
