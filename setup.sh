#!/bin/bash

# Virtual Try-On Setup Script
# This script helps you set up the Virtual Try-On environment

set -e

echo "=================================="
echo "Virtual Try-On Setup Script"
echo "=================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi
echo "✅ Python 3 found: $(python3 --version)"

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo "❌ gcloud CLI is not installed."
    echo "Please install it from: https://cloud.google.com/sdk/docs/install"
    exit 1
fi
echo "✅ gcloud CLI found: $(gcloud --version | head -n 1)"

# Check if user is authenticated
if ! gcloud auth list --filter=status:ACTIVE --format="value(account)" &> /dev/null; then
    echo "⚠️  Not authenticated with gcloud"
    echo "Running: gcloud auth login"
    gcloud auth login
fi
echo "✅ Authenticated with gcloud"

# Check for application default credentials
if ! gcloud auth application-default print-access-token &> /dev/null; then
    echo "⚠️  Application default credentials not set"
    echo "Running: gcloud auth application-default login"
    gcloud auth application-default login
fi
echo "✅ Application default credentials configured"

# Get or set project ID
CURRENT_PROJECT=$(gcloud config get-value project 2>/dev/null || echo "")
if [ -z "$CURRENT_PROJECT" ]; then
    echo ""
    echo "No project is set. Please enter your Google Cloud Project ID:"
    read -r PROJECT_ID
    gcloud config set project "$PROJECT_ID"
    CURRENT_PROJECT="$PROJECT_ID"
fi
echo "✅ Project set: $CURRENT_PROJECT"

# Enable required APIs
echo ""
echo "Enabling Vertex AI API..."
gcloud services enable aiplatform.googleapis.com --project="$CURRENT_PROJECT"
echo "✅ Vertex AI API enabled"

# Set environment variables
echo ""
echo "Setting environment variables..."
export GOOGLE_CLOUD_PROJECT="$CURRENT_PROJECT"
export GOOGLE_CLOUD_REGION="us-central1"

# Add to shell config if not already there
SHELL_CONFIG=""
if [ -f "$HOME/.zshrc" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
elif [ -f "$HOME/.bashrc" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
elif [ -f "$HOME/.bash_profile" ]; then
    SHELL_CONFIG="$HOME/.bash_profile"
fi

if [ -n "$SHELL_CONFIG" ]; then
    if ! grep -q "GOOGLE_CLOUD_PROJECT" "$SHELL_CONFIG"; then
        echo "" >> "$SHELL_CONFIG"
        echo "# Virtual Try-On Environment Variables" >> "$SHELL_CONFIG"
        echo "export GOOGLE_CLOUD_PROJECT=\"$CURRENT_PROJECT\"" >> "$SHELL_CONFIG"
        echo "export GOOGLE_CLOUD_REGION=\"us-central1\"" >> "$SHELL_CONFIG"
        echo "✅ Environment variables added to $SHELL_CONFIG"
    else
        echo "✅ Environment variables already in $SHELL_CONFIG"
    fi
fi

# Create virtual environment
echo ""
echo "Creating Python virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment and install dependencies
echo ""
echo "Installing Python dependencies..."
source venv/bin/activate
pip install --upgrade pip -q
pip install -r requirements.txt -q
echo "✅ Dependencies installed"

# Create directory structure
echo ""
echo "Creating directory structure..."
mkdir -p input_images/person
mkdir -p input_images/clothing
mkdir -p output_images
echo "✅ Directories created"

# Final summary
echo ""
echo "=================================="
echo "✅ Setup Complete!"
echo "=================================="
echo ""
echo "Next steps:"
echo "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Add your images:"
echo "   - Person image: input_images/person/model.jpg"
echo "   - Clothing items: input_images/clothing/*.jpg"
echo ""
echo "3. Run the demo:"
echo "   python virtual_tryon.py"
echo ""
echo "4. Check the output:"
echo "   ls output_images/"
echo ""
echo "For more information, see:"
echo "   - QUICKSTART.md - Quick start guide"
echo "   - README.md - Full documentation"
echo "   - example_usage.py - Usage examples"
echo ""
echo "=================================="
