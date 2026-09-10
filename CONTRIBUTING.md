# Contributing

Thank you for your interest in improving the Affiliate Framework! We welcome contributions that make the framework more useful, reliable, and easier to use.

---

## 📋 Table of Contents

- [Before You Begin](#-before-you-begin)
- [How to Contribute](#-how-to-contribute)
- [Pull Request Process](#-pull-request-process)
- [Code Guidelines](#-code-guidelines)
- [Testing](#-testing)
- [Reporting Issues](#-reporting-issues)

---

## 🎯 Before You Begin

Please review the following before contributing:

1. **Read** this CONTRIBUTING.md file
2. **Read** [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
3. **Read** [SECURITY.md](./SECURITY.md) for security-related contributions
4. **Search** existing issues and pull requests to avoid duplicates

---

## 🤝 How to Contribute

### Reporting Bugs

- Use the GitHub issue tracker
- Include steps to reproduce
- Include expected vs actual behavior
- Include screenshots if applicable
- Include your Python version and OS

### Suggesting Features

- Open a GitHub issue with your feature request
- Explain the use case
- Explain the expected behavior
- Include any relevant examples

### Submitting Code

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Update documentation
6. Commit with clear messages
7. Push to your fork
8. Open a Pull Request to main branch

---

## 📝 Pull Request Process

1. **Title**: Clear and descriptive (use prefix: feat:, fix:, docs:, refactor:)
2. **Description**: Explain what and why
3. **Testing**: Describe how you tested your changes
4. **Screenshots**: Include if UI changes
5. **Checklist**:
   - [ ] All tests pass
   - [ ] Code follows guidelines
   - [ ] Documentation updated
   - [ ] No sensitive data
   - [ ] All links work

Maintainers will review and may request changes before merging.

---

## 💻 Code Guidelines

### Python

- Follow PEP 8 style guide
- Use 4 spaces for indentation
- Use descriptive variable names
- Add docstrings to functions
- Handle errors gracefully
- Validate all inputs

### HTML/CSS

- Use semantic HTML
- Keep CSS organized
- Comment complex styles
- Use relative units (em, rem, %)
- Ensure responsiveness

### JavaScript

- Use modern ES6+ syntax
- Avoid jQuery unless necessary
- Handle errors gracefully
- Validate all inputs

---

## 🧪 Testing

All contributions should be tested:

### Manual Testing

- [ ] Generate site with sample products.json
- [ ] Open generated site in browser
- [ ] Test all links
- [ ] Test on mobile and desktop
- [ ] Validate HTML

### Automated Testing (if applicable)

Run existing tests:
```bash
python3 -m unittest discover
```

---

## 🐛 Reporting Issues

When reporting issues:

- Use clear, descriptive title
- Include steps to reproduce
- Include expected vs actual behavior
- Include screenshots if applicable
- Include your environment (Python version, OS, browser)
- Include relevant code snippets

**Do not** report security vulnerabilities publicly. See [SECURITY.md](./SECURITY.md) for private reporting.

---

## 📚 Additional Resources

- [LICENSE](./LICENSE) - License information
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) - Community guidelines
- [SECURITY.md](./SECURITY.md) - Security policy

---

*Last updated: September 11, 2026*
*Maintainer: Stijnman*
