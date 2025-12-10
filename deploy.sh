#!/bin/bash

# One-command deployment to Google Cloud Run
# Usage: ./deploy.sh

echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║     🚀 Deploying Virtual Try-On to Google Cloud Run                ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""

PROJECT_ID="renderedfitsnew"
REGION="us-central1"
SERVICE_NAME="virtual-tryon"

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo "❌ gcloud CLI not found."
    echo "Install from: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

echo "✅ gcloud CLI found"
echo ""

# Set project
echo "Setting project to: $PROJECT_ID"
gcloud config set project $PROJECT_ID

# Enable APIs
echo ""
echo "Enabling required APIs..."
gcloud services enable run.googleapis.com --project=$PROJECT_ID --quiet
gcloud services enable cloudbuild.googleapis.com --project=$PROJECT_ID --quiet
echo "✅ APIs enabled"

# Deploy to Cloud Run
echo ""
echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║     Deploying to Cloud Run (this takes 2-3 minutes)...             ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""

gcloud run deploy $SERVICE_NAME \
  --source . \
  --project=$PROJECT_ID \
  --region=$REGION \
  --platform=managed \
  --allow-unauthenticated \
  --port=8080 \
  --memory=2Gi \
  --cpu=2 \
  --timeout=300 \
  --min-instances=0 \
  --max-instances=10 \
  --set-env-vars="GOOGLE_CLOUD_PROJECT=$PROJECT_ID,GOOGLE_CLOUD_REGION=$REGION" \
  --quiet

if [ $? -eq 0 ]; then
    echo ""
    echo "╔══════════════════════════════════════════════════════════════════════╗"
    echo "║     ✅ DEPLOYMENT SUCCESS!                                          ║"
    echo "╚══════════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "Your Virtual Try-On app is now live on the web!"
    echo ""

    # Get service URL
    SERVICE_URL=$(gcloud run services describe $SERVICE_NAME \
      --project=$PROJECT_ID \
      --region=$REGION \
      --format='value(status.url)')

    echo "🌐 Your app URL:"
    echo "   $SERVICE_URL"
    echo ""
    echo "📊 Monitor your app:"
    echo "   https://console.cloud.google.com/run/detail/$REGION/$SERVICE_NAME?project=$PROJECT_ID"
    echo ""
    echo "💰 Check costs:"
    echo "   https://console.cloud.google.com/billing?project=$PROJECT_ID"
    echo ""
    echo "🔄 To update your app, just run: ./deploy.sh"
    echo ""
    echo "Share the URL with anyone! No installation needed! 🎉"
    echo ""
else
    echo ""
    echo "╔══════════════════════════════════════════════════════════════════════╗"
    echo "║     ❌ DEPLOYMENT FAILED                                            ║"
    echo "╚══════════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "Common issues:"
    echo "  1. Not authenticated - run: gcloud auth login"
    echo "  2. Missing files - check app_deploy.py, virtual_tryon.py, config.py exist"
    echo "  3. API not enabled - should be auto-enabled, check console"
    echo ""
    exit 1
fi
