import json
import os
from pathlib import Path

# Load products
with open('products.json', 'r') as f:
    products = json.load(f)

# Create dist directory
dist_dir = Path('dist')
dist_dir.mkdir(exist_ok=True)

# Template for product page
product_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{product_name} - Affiliate Site</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        .product-image {{
            width: 100%;
            height: auto;
            border-radius: 8px;
        }}
        .price {{
            font-size: 24px;
            color: #e74c3c;
            margin: 20px 0;
        }}
        .affiliate-link {{
            display: inline-block;
            background-color: #3498db;
            color: white;
            padding: 12px 24px;
            text-decoration: none;
            border-radius: 4px;
            font-weight: bold;
        }}
        .affiliate-link:hover {{
            background-color: #2980b9;
        }}
        .back-link {{
            margin-top: 30px;
            display: inline-block;
            color: #7f8c8d;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{product_name}</h1>
        <img src="{image_url}" alt="{product_name}" class="product-image">
        <p>{description}</p>
        <p class="price">{price}</p>
        <a href="{affiliate_link}" target="_blank" class="affiliate-link">Buy Now</a>
        <a href="index.html" class="back-link">← Back to all products</a>
    </div>
</body>
</html>
'''

# Template for index page
index_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Affiliate Product Site</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
        }}
        h1 {{
            text-align: center;
            color: #2c3e50;
        }}
        .product-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}
        .product-card {{
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }}
        .product-card:hover {{
            transform: translateY(-5px);
        }}
        .product-image {{
            width: 100%;
            height: 200px;
            object-fit: cover;
        }}
        .product-info {{
            padding: 15px;
        }}
        .product-title {{
            font-size: 18px;
            margin: 0 0 10px 0;
            color: #2c3e50;
        }}
        .product-description {{
            color: #7f8c8d;
            font-size: 14px;
            margin: 0 0 10px 0;
        }}
        .product-price {{
            font-size: 20px;
            color: #e74c3c;
            font-weight: bold;
        }}
        .affiliate-link {{
            display: block;
            text-align: center;
            background-color: #3498db;
            color: white;
            padding: 10px;
            text-decoration: none;
            margin-top: 10px;
            border-radius: 4px;
        }}
        .affiliate-link:hover {{
            background-color: #2980b9;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Featured Products</h1>
        <div class="product-grid">
            {product_cards}
        </div>
    </div>
</body>
</html>
'''

# Generate product cards for index
product_cards = ''
for product in products:
    product_cards += f'''
        <div class="product-card">
            <img src="{product['image_url']}" alt="{product['name']}" class="product-image">
            <div class="product-info">
                <h2 class="product-title">{product['name']}</h2>
                <p class="product-description">{product['description']}</p>
                <p class="product-price">{product['price']}</p>
                <a href="product/{product['id']}.html" class="affiliate-link">View Product</a>
            </div>
        </div>
    '''

# Write index.html
with open(dist_dir / 'index.html', 'w') as f:
    f.write(index_template.format(product_cards=product_cards))

# Write product pages
for product in products:
    product_dir = dist_dir / 'product'
    product_dir.mkdir(exist_ok=True)
    with open(product_dir / f"{product['id']}.html", 'w') as f:
        f.write(product_template.format(
            product_name=product['name'],
            description=product['description'],
            price=product['price'],
            image_url=product['image_url'],
            affiliate_link=product['affiliate_link']
        ))

print(f"Generated site for {len(products)} products in {dist_dir}")