#!/usr/bin/env python
# coding: utf-8

# In[4]:


# ============================================
# GENERATE DATA
# ============================================

get_ipython().system('pip install faker')

import pandas as pd
import random
from faker import Faker
import os

fake = Faker()

# --------------------------------
# CONFIG
# --------------------------------
NUM_RECORDS = 100000   # full data (local use)
SAMPLE_SIZE = 1000     # GitHub sample


# In[5]:


# --------------------------------
# CREATE FOLDERS
# --------------------------------
os.makedirs("data/bronze", exist_ok=True)
os.makedirs("data/sample_data", exist_ok=True)


# In[6]:


# --------------------------------
# CUSTOMERS DATA
# --------------------------------
customers = []
for i in range(NUM_RECORDS):
    customers.append({
        "customer_id": i,
        "name": fake.name(),
        "email": fake.email(),
        "country": fake.country(),
        "signup_date": fake.date_between(start_date='-3y', end_date='today')
    })

customers_df = pd.DataFrame(customers)


# In[7]:


# Save FULL data (for ETL)
customers_df.to_csv("data/bronze/customers.csv", index=False)

# Save SAMPLE (for GitHub)
customers_df.head(SAMPLE_SIZE).to_csv("data/sample_data/customers_sample.csv", index=False)


# In[8]:


# --------------------------------
# PRODUCTS DATA
# --------------------------------
categories = ["Electronics", "Clothing", "Home", "Sports"]

products = []
for i in range(500):
    products.append({
        "product_id": i,
        "product_name": fake.word(),
        "category": random.choice(categories),
        "price": round(random.uniform(10, 1000), 2)
    })

products_df = pd.DataFrame(products)

products_df.to_csv("data/bronze/products.csv", index=False)
products_df.head(200).to_csv("data/sample_data/products_sample.csv", index=False)


# In[9]:


# --------------------------------
# ORDERS DATA
# --------------------------------
orders = []
for i in range(NUM_RECORDS):
    orders.append({
        "order_id": i,
        "customer_id": random.randint(0, NUM_RECORDS - 1),
        "product_id": random.randint(0, 499),
        "quantity": random.randint(1, 5),
        "order_date": fake.date_between(start_date='-1y', end_date='today'),
        "status": random.choice(["Shipped", "Pending", "Cancelled"])
    })

orders_df = pd.DataFrame(orders)

orders_df.to_csv("data/bronze/orders.csv", index=False)
orders_df.head(SAMPLE_SIZE).to_csv("data/sample_data/orders_sample.csv", index=False)


# In[10]:


# --------------------------------
# DONE
# --------------------------------
print("✅ Data generated successfully!")
print("📁 Full data → data/bronze/")
print("📁 Sample data → data/sample_data/")


# In[ ]:




