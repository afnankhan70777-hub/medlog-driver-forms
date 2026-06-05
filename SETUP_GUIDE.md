# MEDLOG Driver Forms - GitHub Pages Setup Guide

## Overview
This creates free HTML forms hosted on GitHub Pages that work in WhatsApp groups.

## Step 1: Create Formspree Account (5 minutes)

1. Go to https://formspree.io/register
2. Sign up with your email (afnan-ops@shahenexpress.com)
3. Verify your email
4. Create 9 new forms (one per vendor):
   - Jadeer Form
   - Al Shaks Form
   - Dalel Aljawda Form
   - Move Time Form
   - Sadan Form
   - Safe GeNSET Form
   - Modern East Form
   - Al turq Form
   - Safe Journey Form

5. For each form, copy the Form ID (looks like: `xrgdvepl`)

## Step 2: Update HTML Files

For each HTML file, replace `FORMSPREE_ID` with actual form ID:

Example:
```html
<form action="https://formspree.io/f/xrgdvepl" method="POST">
```

## Step 3: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `medlog-driver-forms`
3. Make it **Public**
4. Check "Add a README file"
5. Click "Create repository"

## Step 4: Upload Files

1. In your new repo, click "Add file" → "Upload files"
2. Upload all 9 HTML files:
   - jadeer.html
   - al_shaks.html
   - dalel_aljawda.html
   - move_time.html
   - sadan.html
   - safe_genset.html
   - modern_east.html
   - al_turq.html
   - safe_journey.html

3. Click "Commit changes"

## Step 5: Enable GitHub Pages

1. Go to repository Settings
2. Scroll down to "Pages" section
3. Source: Deploy from a branch
4. Branch: main / root
5. Click "Save"
6. Wait 2-3 minutes for site to deploy

## Step 6: Get Public URLs

Your forms will be at:
- https://YOUR_USERNAME.github.io/medlog-driver-forms/jadeer.html
- https://YOUR_USERNAME.github.io/medlog-driver-forms/al_shaks.html
- etc.

## Step 7: Send to WhatsApp

1. Copy each form URL
2. Send to respective vendor WhatsApp groups
3. Drivers can fill out on their phones

## How It Works

- Driver opens link in WhatsApp
- Fills form on their phone
- Clicks Submit
- Data goes to your Formspree dashboard
- Photos attached to email
- You get email notification

## Viewing Responses

1. Go to https://formspree.io/forms
2. Click on each form
3. View submissions or export to Excel

## Costs

- **GitHub Pages:** FREE
- **Formspree:** FREE (50 submissions/month per form)
- **Total:** $0

## Need Help?

If you get stuck on any step, let me know which one and I'll help!