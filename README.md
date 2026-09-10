# Affiliate Framework

This is a complete affiliate website framework. To use it:

1. Add products to `products.json`
2. Run `python3 generate_site.py` to generate the static site
3. Deploy the `dist/` folder to any static host (GitHub Pages, Netlify, etc.)

## Products Format

```json
[
  {
    "id": "unique-id",
    "name": "Product Name",
    "description": "Product description",
    "price": "$29.99",
    "affiliate_link": "https://your-affiliate-link.com",
    "image_url": "https://example.com/image.jpg"
  }
]
```

## Deployment

For GitHub Pages:
1. Push the `dist/` folder to a gh-pages branch
2. Or use the GitHub Pages action to build and deploy

The framework is completely autonomous - add products, generate site, deploy.