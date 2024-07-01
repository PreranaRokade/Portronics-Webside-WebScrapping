#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

# Fetch the page content
page = requests.get("https://www.portronics.com")
soup = BeautifulSoup(page.content, 'html.parser')

# Initialize lists to store data
product_names = []
product_details = []
prices = []
regular_prices = []
discounts = []
quick_adds = []

# Extract product names
products = soup.find_all(class_="card__heading h5")[3:13]
for product in products:
    product_names.append(product.text.strip())

# Extract product details
details = soup.find_all(class_="card-detail")[3:13]
for detail in details:
    product_details.append(detail.text.strip())

# Extract prices
prices_data = soup.find_all(class_="money")[3:13]
for price in prices_data:
    prices.append(price.text.strip())

# Extract regular prices
regular_prices_data = soup.find_all(class_="price-item price-item--regular")[3:13]
for regular_price in regular_prices_data:
    regular_prices.append(regular_price.text.strip())

# Extract discounts
discounts_data = soup.find_all(class_="discount-percentage")[3:13]
for discount in discounts_data:
    discounts.append(discount.text.strip())

# Extract quick add elements
quick_add_data = soup.find_all(class_="quick-add mt-3 no-js-hidden")[3:13]
for quick_add in quick_add_data:
    quick_adds.append(quick_add.text.strip())

# Ensure all lists have the same length
max_length = max(len(product_names), len(product_details), len(prices), len(regular_prices), len(discounts), len(quick_adds))

# Pad lists to the same length
product_names += [''] * (max_length - len(product_names))
product_details += [''] * (max_length - len(product_details))
prices += [''] * (max_length - len(prices))
regular_prices += [''] * (max_length - len(regular_prices))
discounts += [''] * (max_length - len(discounts))
quick_adds += [''] * (max_length - len(quick_adds))

# Arrange data in a table
table_data = []
for idx, (name, detail, price, regular_price, discount, quick_add) in enumerate(zip(product_names, product_details, prices, regular_prices, discounts, quick_adds), start=1):
    table_data.append([idx, name, detail, price, regular_price, discount, quick_add])

# Print the table
print(tabulate(table_data[:10], headers=["Sr. No.", "Product Name", "Details", "Price", "Regular Price", "Discount", "Quick Add"], tablefmt="grid"))


# In[14]:


import pandas as pd
# Create a DataFrame
earbuddy = pd.DataFrame({
    "Product Name": product_names,
    "Details": product_details,
    "Price": prices,
    "Regular Price": regular_prices,
    "Discount": discounts,
    "Quick Add": quick_adds
})
earbuddy


# In[5]:


import csv

print(f"Data has been saved to {csv_filename}")

