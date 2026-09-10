# Testing Guide

This document outlines the testing requirements and best practices for the Affiliate Framework project.

---

## 📋 Table of Contents

- [Testing Philosophy](#-testing-philosophy)
- [Testing Levels](#-testing-levels)
- [Manual Testing](#-manual-testing)
- [Automated Testing](#-automated-testing)
- [Test Data](#-test-data)
- [Deployment Testing](#-deployment-testing)

---

## 🎯 Testing Philosophy

### Core Principles

1. **Safety First**: Never test with production affiliate links or real data
2. **Validation**: All product data must be validated
3. **Sanitization**: All HTML output must be sanitized to prevent XSS
4. **Completeness**: Test all features and edge cases
5. **Cross-browser**: Test on multiple browsers

### What Must Be Tested

Every change **MUST** be tested for:
- ✅ Successful site generation
- ✅ All product data is displayed correctly
- ✅ All links work (especially affiliate links)
- ✅ No XSS vulnerabilities
- ✅ Responsive design on mobile/desktop
- ✅ Valid HTML output

---

## 🏗️ Testing Levels

### Level 1: Unit Testing (Optional)

Test individual functions in `generate_site.py`:

```python
# test_generator.py
import unittest
from generate_site import load_products, generate_html

class TestGenerator(unittest.TestCase):
    def test_load_products(self):
        """Test loading products from JSON"""
        products = load_products('products.json')
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 0)
    
    def test_generate_html(self):
        """Test HTML generation"""
        product = {
            'id': 'test',
            'name': 'Test Product',
            'description': 'Test Description'
        }
        html = generate_html(product)
        self.assertIn('Test Product', html)
        self.assertIn('Test Description', html)

if __name__ == '__main__':
    unittest.main()
```

### Level 2: Integration Testing

Test the complete site generation process:

```python
# test_site_generation.py
import os
import shutil
from generate_site import generate_site

def test_complete_generation():
    """Test complete site generation"""
    # Setup
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    
    # Generate
    generate_site()
    
    # Verify
    assert os.path.exists('dist/index.html')
    assert os.path.exists('dist/product/')
    
    # Cleanup
    shutil.rmtree('dist')
```

### Level 3: End-to-End Testing

Test the complete workflow:

1. Add test products to products.json
2. Run generate_site.py
3. Open dist/index.html in browser
4. Click all links
5. Verify all products display correctly

---

## 👤 Manual Testing

### Required Manual Tests

#### Site Generation
- [ ] Generate site with empty products.json
- [ ] Generate site with single product
- [ ] Generate site with multiple products
- [ ] Generate site with all optional fields
- [ ] Generate site with special characters in data
- [ ] Generate site with long descriptions

#### Template Testing
- [ ] Main index.html template renders correctly
- [ ] Individual product pages render correctly
- [ ] All template placeholders are replaced
- [ ] Custom templates work (if added)

#### Link Testing
- [ ] All affiliate links work
- [ ] All internal links work
- [ ] Links open in correct target (blank/new tab)
- [ ] No broken links

#### Responsive Testing
- [ ] Site displays correctly on desktop
- [ ] Site displays correctly on tablet
- [ ] Site displays correctly on mobile
- [ ] Images scale appropriately
- [ ] Text is readable on all devices

#### Edge Cases
- [ ] Empty products.json
- [ ] Products with missing required fields
- [ ] Products with special characters
- [ ] Products with long names/descriptions
- [ ] Products with no image
- [ ] Products with broken image URLs

### Manual Testing Checklist

```markdown
# Testing Checklist: [Feature/Change]

## Setup
- [ ] Test environment configured
- [ ] Test products.json created
- [ ] Previous test state cleaned up

## Generation Tests
- [ ] Site generates without errors
- [ ] All products included in output
- [ ] All required fields present
- [ ] Optional fields handled gracefully
- [ ] No errors or warnings

## Output Tests
- [ ] dist/index.html exists
- [ ] dist/product/ directory exists
- [ ] Individual product pages exist
- [ ] HTML is valid (W3C validator)
- [ ] No broken links
- [ ] All images load

## Browser Tests
- [ ] Chrome: Site displays correctly
- [ ] Firefox: Site displays correctly
- [ ] Safari: Site displays correctly
- [ ] Mobile Chrome: Site displays correctly
- [ ] Mobile Safari: Site displays correctly

## Link Tests
- [ ] All affiliate links work
- [ ] All internal links work
- [ ] Links open correctly
- [ ] No 404 errors

## Security Tests
- [ ] No XSS vulnerabilities
- [ ] No sensitive data exposed
- [ ] All URLs use HTTPS
- [ ] Input data is sanitized

## Cleanup
- [ ] Test files removed
- [ ] Environment restored

## Results
- [ ] All tests passed
- [ ] Issues found: _______________
- [ ] Notes: _____________________
```

---

## 🤖 Automated Testing

### Running Tests

```bash
# Run all unit tests
python3 -m unittest discover

# Run specific test file
python3 -m unittest test_generator.py

# Run with verbose output
python3 -m unittest discover -v
```

---

## 📊 Test Data

### Sample Products for Testing

```json
[
  {
    "id": "test-product-1",
    "name": "Test Product 1",
    "description": "This is a test product description.",
    "price": "$29.99",
    "affiliate_link": "https://example.com/test?ref=test",
    "image_url": "https://example.com/test-image.jpg",
    "category": "Test Category",
    "rating": 4.5,
    "features": ["Feature 1", "Feature 2", "Feature 3"],
    "tags": ["test", "sample"]
  },
  {
    "id": "test-product-2",
    "name": "Test Product with Special Chars: <>&\"'",
    "description": "Description with special characters: <>&\"'",
    "price": "$49.99",
    "affiliate_link": "https://example.com/test2?ref=test",
    "image_url": "https://example.com/test-image2.jpg"
  },
  {
    "id": "test-product-3",
    "name": "Test Product with Long Description",
    "description": "Very long description that tests how the site handles long text...",
    "price": "$99.99",
    "affiliate_link": "https://example.com/test3?ref=test",
    "image_url": "https://example.com/test-image3.jpg"
  }
]
```

### Test Data Principles

1. Use fake data only
2. Use example.com for test URLs
3. Use test affiliate links
4. Clean up after testing

---

## 🚀 Deployment Testing

### GitHub Pages Testing

1. Generate site locally
2. Push to gh-pages branch
3. Wait for GitHub Pages deployment
4. Visit the live site
5. Verify all features work

### Netlify Testing

1. Connect repository to Netlify
2. Configure build settings
3. Deploy
4. Visit the live site
5. Verify all features work

### Local Testing

1. Generate site: `python3 generate_site.py`
2. Start local server: `python3 -m http.server 8000 --directory dist`
3. Open in browser: `http://localhost:8000`
4. Test all features

---

## ✅ Test Checklists

### Pre-Commit Checklist

Before committing:
- [ ] Code follows guidelines
- [ ] All tests pass
- [ ] No sensitive data
- [ ] Documentation updated
- [ ] All links work

### Pre-PR Checklist

Before opening a PR:
- [ ] All manual tests pass
- [ ] Automated tests pass (if applicable)
- [ ] Code follows guidelines
- [ ] Documentation is complete
- [ ] No sensitive data
- [ ] Version numbers updated (if applicable)

### Pre-Release Checklist

Before creating a release:
- [ ] All tests pass
- [ ] All PRs merged
- [ ] CHANGELOG.md updated
- [ ] Version numbers updated
- [ ] Documentation is complete
- [ ] Breaking changes documented

---

## 🛠️ Test Utilities

### HTML Validation

Use W3C validator:
```bash
# Install html5validator
pip install html5validator

# Validate generated HTML
html5validator --root dist/
```

### Link Checking

Use linkchecker:
```bash
pip install linkchecker
linkchecker http://localhost:8000
```

---

## 🎯 Summary

| Aspect | Requirement |
|--------|-------------|
| Manual Testing | ✅ Required for all changes |
| Automated Testing | ⚠️ Recommended for core functionality |
| Test Coverage | Test all features |
| Test Data | Fake data only |
| Validation | ✅ Required for all PRs |

**Remember**: Thorough testing ensures the framework works reliably for all users.

---

*Last updated: September 11, 2026*
*Maintainer: Stijnman*
