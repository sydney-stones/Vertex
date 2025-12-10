#!/bin/bash

# Automated Hugging Face Deployment Script
# Usage: ./deploy_to_hf.sh

echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║     🚀 Deploy Virtual Try-On to Hugging Face                        ║"
echo "║     Space: sydstones02/vertex                                       ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""

HF_SPACE="https://huggingface.co/spaces/sydstones02/vertex"
PROJECT_ID="renderedfitsnew"

# Step 1: Clone the space
echo "📥 Step 1: Cloning your Hugging Face Space..."
echo ""

if [ -d "vertex" ]; then
    echo "⚠️  Directory 'vertex' already exists."
    read -p "Delete and re-clone? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf vertex
    else
        echo "Using existing directory..."
        cd vertex
    fi
fi

if [ ! -d "vertex" ]; then
    echo "Cloning space..."
    echo "When prompted for password, use your Hugging Face access token"
    echo "Get token from: https://huggingface.co/settings/tokens"
    echo ""
    git clone $HF_SPACE
    cd vertex
fi

echo "✅ Space cloned"
echo ""

# Step 2: Copy files
echo "📋 Step 2: Copying application files..."
echo ""

cp ../app_deploy.py app.py
cp ../virtual_tryon.py .
cp ../config.py .
cp ../requirements.txt .

echo "✅ Files copied:"
echo "   - app.py"
echo "   - virtual_tryon.py"
echo "   - config.py"
echo "   - requirements.txt"
echo ""

# Step 3: Generate credentials
echo "🔐 Step 3: Generating Google Cloud credentials..."
echo ""

if [ -f "../credentials.json" ]; then
    echo "⚠️  credentials.json already exists"
    read -p "Generate new credentials? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Using existing credentials..."
        cp ../credentials.json .
    fi
fi

if [ ! -f "credentials.json" ]; then
    cd ..

    echo "Creating service account..."
    gcloud iam service-accounts create virtual-tryon-sa \
      --project=$PROJECT_ID \
      --display-name="Virtual Try-On Service Account" 2>/dev/null || echo "Service account may already exist"

    echo "Granting permissions..."
    gcloud projects add-iam-policy-binding $PROJECT_ID \
      --member="serviceAccount:virtual-tryon-sa@$PROJECT_ID.iam.gserviceaccount.com" \
      --role="roles/aiplatform.user" \
      --condition=None > /dev/null 2>&1

    echo "Creating key..."
    gcloud iam service-accounts keys create credentials.json \
      --iam-account=virtual-tryon-sa@$PROJECT_ID.iam.gserviceaccount.com

    cd vertex
    cp ../credentials.json .
fi

echo "✅ Credentials ready"
echo ""

# Step 4: Instructions for secrets
echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║     🔑 IMPORTANT: Add Secrets to Hugging Face                       ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""
echo "Open this URL in your browser:"
echo "  https://huggingface.co/spaces/sydstones02/vertex/settings"
echo ""
echo "Click 'Repository secrets' and add these two secrets:"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Secret #1:"
echo "  Name:  GOOGLE_CLOUD_PROJECT"
echo "  Value: renderedfitsnew"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Secret #2:"
echo "  Name:  GOOGLE_APPLICATION_CREDENTIALS_JSON"
echo "  Value: (copy ALL text below)"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
cat credentials.json
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 The credentials have also been saved to: credentials.json"
echo ""

read -p "Press ENTER when you've added both secrets to Hugging Face... " -r
echo ""

# Step 5: Commit and push
echo "📤 Step 5: Deploying to Hugging Face..."
echo ""

# Remove credentials from git
echo "credentials.json" >> .gitignore

git add app.py virtual_tryon.py config.py requirements.txt .gitignore
git commit -m "Add Virtual Try-On application"

echo "Pushing to Hugging Face..."
echo "You'll need to enter your access token again as password"
echo ""

git push

if [ $? -eq 0 ]; then
    echo ""
    echo "╔══════════════════════════════════════════════════════════════════════╗"
    echo "║     ✅ DEPLOYMENT SUCCESS!                                          ║"
    echo "╚══════════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "Your app is building now! Watch the progress at:"
    echo "  https://huggingface.co/spaces/sydstones02/vertex"
    echo ""
    echo "Once it shows 'Running', your app is live!"
    echo ""
    echo "🌐 Share this URL with anyone:"
    echo "  https://huggingface.co/spaces/sydstones02/vertex"
    echo ""

    # Clean up credentials
    cd ..
    read -p "Delete local credentials.json? (recommended) (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -f credentials.json
        rm -f vertex/credentials.json
        echo "✅ Credentials deleted (they're safe in HF Secrets)"
    fi

    echo ""
    echo "🎉 Done! Your Virtual Try-On is now on the web!"
    echo ""
else
    echo ""
    echo "╔══════════════════════════════════════════════════════════════════════╗"
    echo "║     ❌ DEPLOYMENT FAILED                                            ║"
    echo "╚══════════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "Common issues:"
    echo "  1. Wrong token - make sure it has 'Write' permissions"
    echo "  2. Not authenticated - get token from https://huggingface.co/settings/tokens"
    echo ""
    exit 1
fi
