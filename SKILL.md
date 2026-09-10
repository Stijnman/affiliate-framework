# Affiliate Framework

**Description**: Complete framework for building static affiliate websites. Generate product pages from JSON data and deploy to any static host including GitHub Pages.

**Purpose**: Enable users to create, manage, and deploy affiliate product websites with minimal effort using a simple JSON-based configuration system.

---

## 🎯 Quick Start

### For Users

1. **Clone** the repository
2. **Edit** `products.json` with your affiliate products
3. **Run** the site generator
4. **Deploy** the `dist/` folder

```bash
# Clone the repository
git clone https://github.com/Stijnman/affiliate-framework.git
cd affiliate-framework

# Edit products.json with your affiliate products
nano products.json

# Generate the static site
python3 generate_site.py

# Deploy to GitHub Pages
# Option 1: Push dist/ to gh-pages branch
git checkout gh-pages
git add dist/
git commit -m "Update affiliate site"
git push origin gh-pages

# Option 2: Use any static host
# Copy dist/ contents to your hosting provider
```

### For Developers

Extend the framework by:
- Modifying `generate_site.py` for custom templates
- Adding new product fields to `products.json`
- Creating custom CSS styles
- Adding JavaScript for enhanced functionality

---

## 📦 Project Structure

```
affiliate-framework/
├── products.json              # Product data (JSON format)
├── generate_site.py          # Site generator script
├── index.html                # Main template file
├── product/                  # Product page templates
│   └── [product-id].html     # Individual product pages
├── dist/                     # Generated static site
│   ├── index.html
│   ├── product/
│   │   └── [product-id].html
│   └── assets/               # CSS, JS, images
└── README.md                 # Documentation
```

---

## 📝 Products Format

Edit `products.json` to add your affiliate products:

```json
[
  {
    "id": "unique-product-id",
    "name": "Product Name",
    "description": "Detailed product description",
    "price": "$29.99",
    "affiliate_link": "https://affiliate-link.com/?ref=your-id",
    "image_url": "https://example.com/product-image.jpg",
    "category": "Product Category",
    "rating": 4.5,
    "features": ["Feature 1", "Feature 2", "Feature 3"],
    "tags": ["tag1", "tag2"]
  }
]
```

### Required Fields
- `id` - Unique identifier (used for filename)
- `name` - Product name
- `description` - Product description
- `affiliate_link` - Your affiliate link
- `image_url` - Product image URL

### Optional Fields
- `price` - Product price
- `category` - Product category
- `rating` - Rating (1-5)
- `features` - Array of features
- `tags` - Array of tags

---

## 🚀 Deployment Options

### GitHub Pages (Recommended)

1. Generate site: `python3 generate_site.py`
2. Switch to gh-pages branch: `git checkout gh-pages`
3. Add generated files: `git add dist/`
4. Commit: `git commit -m "Update affiliate site"`
5. Push: `git push origin gh-pages`

**Note**: GitHub Pages serves from `gh-pages` branch by default.

### Netlify

1. Connect your repository to Netlify
2. Set build command: `python3 generate_site.py`
3. Set publish directory: `dist/`
4. Deploy

### Vercel

1. Import repository to Vercel
2. Set output directory: `dist/`
3. Deploy

### Any Static Host

Copy contents of `dist/` to any web server or static hosting service.

---

## 🔧 Customization

### Templates

Edit `index.html` to customize the main page template. Use the following placeholders:

- `{{title}}` - Page title
- `{{products}}` - Product list HTML
- `{{product.name}}` - Product name
- `{{product.description}}` - Product description
- `{{product.price}}` - Product price
- `{{product.image_url}}` - Product image URL
- `{{product.affiliate_link}}` - Affiliate link

### Styling

Add custom CSS by:
1. Creating a `styles/` folder
2. Adding `style.css` file
3. Linking in your HTML templates

### JavaScript

Add custom JavaScript by:
1. Creating a `scripts/` folder
2. Adding your JS files
3. Linking in your HTML templates

---

## 📚 Documentation

| Document | Description | Required Reading |
|----------|-------------|------------------|
| **[SECURITY.md](./SECURITY.md)** | ⚠️ Security policy and best practices | ✅ All users |
| **[CONTRIBUTING.md](./CONTRIBUTING.md)** | How to contribute improvements | ⚠️ Contributors |
| **[TESTING.md](./TESTING.md)** | Testing requirements and guide | ⚠️ Contributors |
| **[LICENSE](./LICENSE)** | MIT License terms | ✅ All users |
| **[CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)** | Community guidelines | ✅ All users |
| **[CHANGELOG.md](./CHANGELOG.md)** | Version history and changes | ⚠️ All users |

---

## 🔐 Security Considerations

### Affiliate Links
- ⚠️ **Never expose** raw affiliate IDs or API keys in products.json
- ✅ **Use** full affiliate URLs with your referral code embedded
- ✅ **Test** all links before deployment
- ⚠️ **Monitor** for broken links regularly

### Data Validation
- Validate all product data before generating pages
- Sanitize all HTML output to prevent XSS
- Check all URLs are valid and secure (HTTPS)

### Privacy
- Do not collect user data without consent
- If adding analytics, disclose in privacy policy
- Comply with GDPR and other regulations

---

## 🧪 Testing

Test your affiliate site before deployment:

1. **Generate locally**: Run `python3 generate_site.py`
2. **Open in browser**: Open `dist/index.html` in a browser
3. **Test all links**: Click all affiliate links and buttons
4. **Validate HTML**: Use W3C validator
5. **Check responsiveness**: Test on mobile, tablet, desktop
6. **Test forms**: If you add contact forms, test submissions

---

## 🤝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for:
- How to add new features
- How to improve existing code
- Testing requirements
- Pull request process

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for full license text.

**You are free to**:
- Use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
- Use for commercial purposes
- Modify for your own needs

**Under the following conditions**:
- Include copyright notice and license in all copies
- Provide attribution to the original author (Stijnman)

---

## 📞 Support

| Issue Type | How to Get Help | Response Time |
|-----------|-----------------|---------------|
| 🐛 **Bug Report** | [Open a GitHub Issue](https://github.com/Stijnman/affiliate-framework/issues) | 24-48 hours |
| 🔒 **Security Issue** | Private message via GitHub profile | Immediate |
| ❓ **General Question** | [Open a GitHub Discussion](https://github.com/Stijnman/affiliate-framework/discussions) | 24 hours |
| 💡 **Feature Request** | [Open a GitHub Issue](https://github.com/Stijnman/affiliate-framework/issues) | 1 week |

---

## 🏷️ Repository Metadata

| Attribute | Value |
|-----------|-------|
| **Repository** | [affiliate-framework](https://github.com/Stijnman/affiliate-framework) |
| **Owner** | [Stijnman](https://github.com/Stijnman) |
| **License** | MIT |
| **Language** | Python, HTML |
| **Created** | September 2026 |
| **Purpose** | Affiliate website generation |

---

## 🎯 Key Features

| Feature | Description |
|---------|-------------|
| **JSON-based** | Simple JSON configuration for products |
| **Static site** | Fast, secure, no server required |
| **GitHub Pages** | Free hosting included |
| **Customizable** | Edit templates and styles |
| **Extensible** | Add new features easily |
| **Lightweight** | Minimal dependencies |

---

## 📌 Important Notes

### Design Principle
> **Keep it simple**: The framework generates static HTML from JSON. No databases, no backend, no complexity.

### Usage Warning
> **Test thoroughly**: Always test generated sites locally before deploying to production.

### Performance Tip
> **Optimize images**: Compress product images for faster loading and better SEO.

---

*Last updated: September 11, 2026*
*Maintainer: Stijnman*
*Repository: [affiliate-framework](https://github.com/Stijnman/affiliate-framework)*
