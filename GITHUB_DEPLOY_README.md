# Deploy to GitHub Pages - Instructions

## Step 1: Run deploy.sh in Git Bash

1. Open **Git Bash** on your PC
2. Navigate to the driver_forms folder:
   ```bash
   cd /f/office/driver_forms
   ```
3. Run the deploy script:
   ```bash
   ./deploy.sh
   ```

This will commit your files locally.

## Step 2: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `medlog-driver-forms`
3. Make it **PUBLIC**
4. **DO NOT** check "Add a README file"
5. Click **Create repository**

## Step 3: Connect and Push

Back in Git Bash, run:
```bash
./connect_github.sh
```

Enter your GitHub username when prompted.

## Step 4: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** tab
3. Click **Pages** (left sidebar)
4. Under **Source**, select **Deploy from a branch**
5. Select **master** or **main** branch, **/ (root)** folder
6. Click **Save**

## Step 5: Your Forms Are Live!

After 2-3 minutes, access your forms at:
- https://YOUR_USERNAME.github.io/medlog-driver-forms/jadeer.html
- https://YOUR_USERNAME.github.io/medlog-driver-forms/al_shaks.html
- etc.

## Generate Driver Links

Once your site is live, I can create a Python script to generate unique links for each driver with their info pre-filled!
