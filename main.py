import json
import utils

with open('Products.json', 'r') as file:
    product_data = json.load(file)

filtered_data = {}
for product in product_data:
    id = product['product_id']
    filtered_data[id] = {}

    filtered_data[id]['price'] = product['price']
    filtered_data[id]['name'] = product['name']
    filtered_data[id]['category'] = product['category']
    filtered_data[id]['description'] = product['description']

with open("Orders.json", "r") as file:
    order_data = json.load(file)

for order in order_data:
    metadata = {"customer_id": order['customer_id'], "customer_email": order['customer_email']}
    for product in order['products']:

        product_id = product["product_id"]
        text = f"Name: {filtered_data[product_id]['name']}, Category: {filtered_data[product_id]['category']}, Description: {filtered_data[product_id]['description']}"
        vector = utils.text2vector(text)
        
        utils.upsert_pinecone(vector=vector, metadata=metadata)

for id, data in filtered_data.items():
    if utils.check_underselling_products(id):
        updated_price = data['price'] * 0.9
        utils.update_shopify_price(id, updated_price)

        utils.update_db_price(id, updated_price)

        text = f"Name: {filtered_data[id]['name']}, Category: {filtered_data[id]['category']}, Description: {filtered_data[id]['description']}"
        vector = utils.text2vector(text)

        customers = utils.query_pinecone(vector)
        unique_customers = list(set(customers))

        utils.send_email(unique_customers, text, updated_price)

