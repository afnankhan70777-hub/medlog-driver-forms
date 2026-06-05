#!/bin/bash
# Deploy driver forms to GitHub Pages
# Run this in Git Bash

echo "=========================================="
echo "  Deploy Driver Forms to GitHub"
echo "=========================================="
echo ""

# Navigate to driver_forms folder
cd /f/office/driver_forms

# Configure git (local only)
git config user.email "afnan@shahenexpress.com"
git config user.name "Afnan"

# Add all files
echo "Adding files to git..."
git add .

# Commit
echo "Committing files..."
git commit -m "Initial commit of driver forms"

echo ""
echo "=========================================="
echo "  Files committed successfully!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Go to https://github.com/new"
echo "2. Create a new repository named: medlog-driver-forms"
echo "3. Make it PUBLIC"
echo "4. Do NOT initialize with README"
echo "5. After creating, copy the repository URL"
echo "   (looks like: https://github.com/YOUR_USERNAME/medlog-driver-forms.git)"
echo ""
echo "Then come back and run: ./connect_github.sh"
