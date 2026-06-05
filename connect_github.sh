#!/bin/bash
# Connect to GitHub and push files
# Run this AFTER creating the GitHub repository

echo "=========================================="
echo "  Connect to GitHub"
echo "=========================================="
echo ""

# Navigate to driver_forms folder
cd /f/office/driver_forms

echo "Enter your GitHub username:"
read USERNAME

REPO_URL="https://github.com/$USERNAME/medlog-driver-forms.git"

echo ""
echo "Connecting to: $REPO_URL"
echo ""

# Add remote
git remote add origin $REPO_URL

# Push to GitHub
echo "Pushing files to GitHub..."
git push -u origin master || git push -u origin main

echo ""
echo "=========================================="
echo "  Files pushed to GitHub!"
echo "=========================================="
echo ""
echo "Next: Enable GitHub Pages"
echo ""
echo "1. Go to: https://github.com/$USERNAME/medlog-driver-forms/settings/pages"
echo "2. Under 'Source', select 'Deploy from a branch'"
echo "3. Select 'master' or 'main' branch"
echo "4. Click 'Save'"
echo ""
echo "Wait 2-3 minutes, then your forms will be live at:"
echo "https://$USERNAME.github.io/medlog-driver-forms/jadeer.html"
echo ""
