# Security Policy

## Scope

This repository contains code and templates for generating static affiliate websites. Security concerns include:

- Exposure of sensitive data in generated HTML
- Malicious code injection through product data
- Broken or malicious affiliate links
- XSS vulnerabilities in templates
- Privacy violations

## Reporting a Vulnerability

**Do not open a public issue for security vulnerabilities.**

Contact the maintainer privately through the repository owner's GitHub profile and include:

1. The affected file or component
2. A concise description of the vulnerability
3. Steps to reproduce (without exposing sensitive data)
4. Potential impact
5. Suggested mitigation (if available)

Allow reasonable time for response and remediation before public disclosure.

## Security Requirements

### For Contributors

- **Never** include sensitive data in products.json
- **Always** validate and sanitize all inputs
- **Always** use HTTPS for all URLs
- **Never** include API keys or credentials in code
- **Test** all security-related changes thoroughly

### For Users

- **Review** products.json before deployment
- **Test** generated sites locally first
- **Use** HTTPS for all affiliate links
- **Monitor** deployed sites for issues
- **Update** regularly to get security fixes

## Supported Versions

Security fixes are applied to the current main branch. Report issues with:
- Commit SHA
- Python version
- Environment details

## Security Best Practices

| Practice | Requirement |
|----------|-------------|
| Use HTTPS | ✅ All URLs must use HTTPS |
| Validate Inputs | ✅ All product data must be validated |
| Sanitize Output | ✅ All HTML output must be sanitized |
| No Sensitive Data | ✅ No credentials, API keys, or private data |
| Test Locally | ✅ Test all changes locally before deployment |

## Out of Scope

This project does not:
- Provide hosting
- Manage affiliate programs
- Store user data
- Process payments

Reports about third-party services should be directed to those providers.

---

*Last updated: September 11, 2026*
*Maintainer: Stijnman*
