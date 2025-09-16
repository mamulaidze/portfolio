# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a personal portfolio website project designed to showcase projects, skills, and experience. It's a static web project with a clean, modern design and responsive layout.

## Architecture

The project follows a traditional static website structure:

- **`src/`** - Source files for development
- **`public/`** - Public assets and HTML files (main entry point)
- **`assets/`** - General assets (fonts, icons, etc.)
- **`css/`** - Stylesheets and CSS files
- **`js/`** - JavaScript files for interactivity
- **`images/`** - Image assets and media files

The main entry point is expected to be `public/index.html` which serves as the homepage.

## Development Workflow

### Local Development
```bash
# Open the main HTML file in browser for viewing
start public/index.html  # Windows
# OR open file directly in browser

# For development with live reload, consider using:
# Python 3 HTTP server
python -m http.server 8000

# Node.js live-server (if installed)
npx live-server public/

# VS Code Live Server extension
# Right-click on index.html -> "Open with Live Server"
```

### File Structure Management
```bash
# Add new images
# Place in images/ directory and reference in HTML/CSS

# Add new stylesheets
# Create in css/ directory and link in HTML

# Add new JavaScript
# Create in js/ directory and include in HTML
```

### Version Control
```bash
# Check current status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Description of changes"

# View commit history
git log --oneline
```

## Key Development Principles

### File Organization
- Keep HTML files in `public/` directory
- Organize CSS by component or page in `css/` directory
- Group JavaScript by functionality in `js/` directory
- Use descriptive naming for images in `images/` directory
- Store reusable assets in `assets/` directory

### Responsive Design
- Design mobile-first
- Use CSS Grid and Flexbox for layouts
- Test across different screen sizes
- Optimize images for different device densities

### Performance Optimization
- Compress images before adding to `images/`
- Minify CSS and JavaScript for production
- Use semantic HTML for accessibility
- Implement lazy loading for images when appropriate

### Content Sections
Based on the README, the portfolio should include:
- Project showcases
- Skills and experience sections
- Contact information
- Clean, modern design with responsive layout

## Common Tasks

### Adding a New Project
1. Add project images to `images/projects/`
2. Update main HTML file with project details
3. Add project-specific styles to CSS
4. Test responsive layout

### Updating Styles
1. Modify existing CSS files in `css/` directory
2. Test changes across different screen sizes
3. Ensure consistent design language

### Adding Interactive Features
1. Create new JavaScript files in `js/` directory
2. Include scripts in HTML files
3. Test functionality across browsers

## Browser Testing
Since this is a static website:
- Test in Chrome, Firefox, Safari, and Edge
- Verify mobile responsiveness
- Check accessibility compliance
- Validate HTML and CSS

## Deployment Preparation
```bash
# Before deploying, ensure:
# 1. All links work correctly
# 2. Images load properly
# 3. CSS and JS are optimized
# 4. Content is up-to-date
# 5. No console errors in browser

# Common deployment targets:
# - GitHub Pages (gh-pages branch)
# - Netlify (drag and drop or git integration)
# - Vercel
# - Traditional web hosting
```