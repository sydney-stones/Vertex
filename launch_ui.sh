#!/bin/bash

# Launch Virtual Try-On Web UI
# This script starts the Gradio web interface

echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║          Virtual Try-On Web Interface Launcher                      ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""

# Set environment variables
export GOOGLE_CLOUD_PROJECT="renderedfitsnew"
export GOOGLE_CLOUD_REGION="us-central1"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found."
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Check if Gradio is installed
if ! python -c "import gradio" 2>/dev/null; then
    echo "📦 Installing dependencies (including Gradio)..."
    pip install -q --upgrade pip
    pip install -q -r requirements.txt
    echo "✅ Dependencies installed!"
fi

# Check authentication
echo ""
echo "Checking Google Cloud authentication..."
if python -c "from google import genai; genai.Client(vertexai=True, project='renderedfitsnew', location='us-central1')" 2>/dev/null; then
    echo "✅ Authentication verified!"
else
    echo "⚠️  Authentication may not be configured."
    echo ""
    echo "If you see errors, run:"
    echo "  gcloud auth application-default login"
    echo ""
fi

echo ""
echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║  Starting Virtual Try-On Web Interface...                           ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""
echo "🌐 The web interface will open at: http://127.0.0.1:7860"
echo ""
echo "Press Ctrl+C to stop the server."
echo ""
echo "─────────────────────────────────────────────────────────────────────"
echo ""

# Launch the app
python app.py
