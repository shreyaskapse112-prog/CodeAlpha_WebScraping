import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send request to website
response = requests.get(url)

print("Website Status Code:", response.status_code)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Store scraped data
books = []

# Extract book information
for book in soup.select("article.product_pod"):

    title = book.h3.a["title"]
    price = book.select_one(".price_color").text.strip()
    availability = book.select_one(".availability").text.strip()

    books.append({
        "Book Name": title,
        "Price": price,
        "Availability": availability
    })

# Create DataFrame
df = pd.DataFrame(books)

# Display data
print("Total Books Scraped:", len(df))
print(df)

# Save dataset
df.to_csv("books_dataset.csv", index=False)

print("Dataset saved successfully!")
