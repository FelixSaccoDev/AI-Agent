import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima

import requests
from dotenv import load_dotenv
import os
import uuid

from pinecone.grpc import PineconeGRPC as Pinecone

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
pinecone_index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))

data = pd.read_json('Orders.json')

data['order_date'] = pd.to_datetime(data['order_date'])
data.set_index('order_date', inplace=True)

# Expand the products list into a DataFrame
products_df = data.explode('products')

# Extract relevant fields from the products DataFrame
products_df['product_id'] = products_df['products'].apply(lambda x: x['product_id'])
products_df['quantity'] = products_df['products'].apply(lambda x: x['quantity'])

# Group by order_date and product_id, summing the quantities
quantity_data = products_df.groupby(['order_date', 'product_id'])['quantity'].sum().reset_index()

# Pivot the data to have a time series for each product
pivot_data = quantity_data.pivot(index='order_date', columns='product_id', values='quantity').fillna(0)

def check_underselling_products(product_id):
    try:
        data_series = pivot_data[product_id]
    
        # Determine Best ARIMA Order
        auto_model = auto_arima(data_series, seasonal=False, trace=True, error_action='ignore', suppress_warnings=True, stepwise=True)
    
        # Fit ARIMA Model
        model = ARIMA(data_series, order=auto_model.order)
        model_fit = model.fit()
    
        # Forecast Future Values
        forecast_days = 10  # Adjust as needed
        forecast = model_fit.forecast(steps=forecast_days)
    
        # Calculate current amount and amount after 10 days
        current_amount = data_series.iloc[-1]  # Latest available amount (quantity sold)
        amount_after_10_days = forecast.iloc[-1]  # Forecasted amount after 10 days
    
        # Calculate the difference
        difference = amount_after_10_days - current_amount
    
        if (difference > 0):
            return False
        else :
            return True
    except:
        return False

def text2vector(text):
    model_id = "sentence-transformers/all-MiniLM-L6-v2"
    hf_token = os.getenv("HF_API_KEY")

    api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
    headers = {"Authorization": f"Bearer {hf_token}"}

    response = requests.post(api_url, headers=headers, json={"inputs": [text], "options":{"wait_for_model":True}})

    data = response.json()

    return data[0]

def update_shopify_price(variant_id: str, new_price: float):
    pass

def update_db_price(product_id: str, new_price: float):
    pass

def upsert_pinecone(vector, metadata):
    id = str(uuid.uuid4())

    pinecone_index.upsert(
        vectors=[
            {
                "id": id, 
                "values": vector, 
                "metadata": metadata
            }
        ]
    )

def query_pinecone(vector):

    result = pinecone_index.query(
        vector=vector,
        top_k=4,
        include_metadata=True
    )

    emails = [match['metadata']['customer_email'] for match in result['matches']]

    return emails

def send_email(emails, text, new_price):
    sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))

    for email in emails:
        message = Mail(
            from_email='rich.alpha425@gmail.com',  
            to_emails=email,
            subject='Discount notification',
            html_content=f'<strong>{text}\nThis product is discounted to {new_price}</strong>'
        )

        try:
            sg.send(message)
        except Exception as e:
            print("Error sending email:", e.message)
