from bs4 import BeautifulSoup
import json

html_doc = """
<html>
<body>
  <h1>Product List</h1>
  <div class="product" data-id="101">
    <span class="name">Widget A</span>
    <span class="price">$10.99</span>
  </div>
  <div class="product" data-id="102">
    <span class="name">Widget B</span>
    <span class="price">$25.50</span>
  </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
products = []

for div in soup.find_all("div", class_="product"):
    products.append({
        "id": div["data-id"],
        "name": div.find("span", class_="name").text,
        "price": div.find("span", class_="price").text
    })

with open("/output/products.json", "w") as f:
    json.dump(products, f, indent=2)
