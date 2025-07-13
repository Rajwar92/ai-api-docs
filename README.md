# AI-Powered API Documentation

A modern, AI-enhanced API documentation site built with MkDocs and Material for MkDocs. This project showcases technical writing skills and modern tooling expertise.

## 🚀 Features

- **Modern Design**: Clean, responsive design with Material for MkDocs theme
- **AI-Enhanced**: Interactive examples and intelligent documentation
- **Search**: Full-text search across all documentation
- **Dark/Light Mode**: Toggle between themes
- **Code Highlighting**: Syntax highlighting for multiple languages
- **Interactive Examples**: Try API calls directly from the docs
- **Mobile Responsive**: Works perfectly on all devices
- **SEO Optimized**: Built-in SEO features and meta tags

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-api-docs.git
   cd ai-api-docs
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run locally**
   ```bash
   mkdocs serve
   ```

4. **Open your browser**
   Navigate to `http://127.0.0.1:8000`

## 📁 Project Structure

```
ai-api-docs/
├── docs/                          # Documentation source files
│   ├── index.md                   # Home page
│   ├── getting-started/           # Getting started guides
│   ├── api-reference/             # API documentation
│   ├── examples/                  # Code examples
│   ├── guides/                    # How-to guides
│   ├── tutorials/                 # Step-by-step tutorials
│   ├── tools/                     # Development tools
│   ├── support/                   # Support documentation
│   ├── assets/                    # Images and static files
│   ├── stylesheets/               # Custom CSS
│   └── javascripts/               # Custom JavaScript
├── mkdocs.yml                     # MkDocs configuration
├── requirements.txt               # Python dependencies
├── netlify.toml                   # Netlify deployment config
└── README.md                      # This file
```

## 🎨 Customization

### Adding New Pages

1. Create a new Markdown file in the appropriate directory
2. Add the page to the navigation in `mkdocs.yml`
3. Use the Material theme features for enhanced formatting

### Styling

- Custom CSS: `docs/stylesheets/extra.css`
- Custom JavaScript: `docs/javascripts/mathjax.js`
- Theme customization: Edit `mkdocs.yml` under the `theme` section

### Configuration

The main configuration file is `mkdocs.yml`. Key sections:

- **Site Information**: Name, description, URL
- **Theme**: Material theme with custom features
- **Navigation**: Site structure and menu
- **Plugins**: Search, Swagger UI, and more
- **Extensions**: Markdown extensions for enhanced content

## 🚀 Deployment

### Netlify (Recommended)

1. **Connect your repository**
   - Push your code to GitHub/GitLab
   - Connect the repository to Netlify

2. **Configure build settings**
   - Build command: `mkdocs build`
   - Publish directory: `site`
   - Python version: 3.9

3. **Deploy**
   - Netlify will automatically build and deploy your site
   - Custom domain can be configured in Netlify settings

### Manual Deployment

1. **Build the site**
   ```bash
   mkdocs build
   ```

2. **Upload to your web server**
   - Upload the contents of the `site/` directory
   - Configure your web server to serve static files

## 🔧 Development

### Local Development

```bash
# Start development server
mkdocs serve

# Build for production
mkdocs build

# Clean build directory
mkdocs build --clean
```

### Adding Content

1. **API Documentation**: Add new endpoints to `docs/api-reference/`
2. **Examples**: Create language-specific examples in `docs/examples/`
3. **Guides**: Write how-to guides in `docs/guides/`
4. **Tutorials**: Create step-by-step tutorials in `docs/tutorials/`

### Best Practices

- Use consistent formatting and structure
- Include code examples for all endpoints
- Add proper error handling examples
- Keep content up-to-date with API changes
- Use descriptive file names and URLs

## 📚 Documentation Features

### Code Examples

```markdown
=== "JavaScript"
    ```javascript
    const response = await fetch('/api/endpoint');
    ```

=== "Python"
    ```python
    response = requests.get('/api/endpoint')
    ```

=== "cURL"
    ```bash
    curl -X GET /api/endpoint
    ```
```

### Admonitions

```markdown
!!! note "Note"
    This is a note.

!!! warning "Warning"
    This is a warning.

!!! tip "Pro Tip"
    This is a helpful tip.
```

### Tables

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: Check the [docs](https://your-site.netlify.app)
- **Issues**: [GitHub Issues](https://github.com/your-username/ai-api-docs/issues)
- **Discord**: [Join our community](https://discord.gg/your-community)
- **Email**: support@example.com

## 🙏 Acknowledgments

- [MkDocs](https://www.mkdocs.org/) - Static site generator
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) - Beautiful theme
- [Netlify](https://netlify.com/) - Hosting and deployment
- [Font Awesome](https://fontawesome.com/) - Icons

---

**Built with ❤️ for developers** 