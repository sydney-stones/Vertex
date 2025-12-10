# Quick Start Guide

Get up and running with Virtual Try-On in 5 minutes!

## Prerequisites Checklist

- [ ] Google Cloud account with billing enabled
- [ ] Python 3.8 or higher installed
- [ ] gcloud CLI installed

## Step-by-Step Setup

### 1. Authenticate with Google Cloud (2 minutes)

```bash
# Login to Google Cloud
gcloud auth login

# Set up application default credentials
gcloud auth application-default login

# Set your project (replace YOUR_PROJECT_ID)
gcloud config set project YOUR_PROJECT_ID
```

### 2. Enable APIs (1 minute)

```bash
gcloud services enable aiplatform.googleapis.com
```

### 3. Set Environment Variables (1 minute)

```bash
# Set your project ID
export GOOGLE_CLOUD_PROJECT="your-project-id"

# Make it permanent (add to your shell config)
echo 'export GOOGLE_CLOUD_PROJECT="your-project-id"' >> ~/.zshrc
source ~/.zshrc
```

### 4. Install Dependencies (1 minute)

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### 5. Add Your Images

```bash
# Directories are auto-created, but you can create them manually:
mkdir -p input_images/person
mkdir -p input_images/clothing
```

Add your images:
- **Person image**: `input_images/person/model.jpg`
- **Clothing items**: `input_images/clothing/shirt.jpg`

### 6. Run Your First Try-On!

```bash
python virtual_tryon.py
```

## Quick Test

Test with a single command:

```python
python3 << EOF
from virtual_tryon import VirtualTryOn

vto = VirtualTryOn()
result = vto.try_on_single_item(
    person_image_path='input_images/person/model.jpg',
    clothing_image_path='input_images/clothing/shirt.jpg'
)
print(f'Success! Image saved: {result[0]}')
EOF
```

## What's Next?

- Read the full [README.md](README.md) for detailed documentation
- Check out [example_usage.py](example_usage.py) for more examples
- Customize settings in [config.py](config.py)

## Common Issues

**"Project ID not set"**
```bash
export GOOGLE_CLOUD_PROJECT="your-project-id"
```

**"Permission denied"**
```bash
gcloud auth application-default login
```

**"API not enabled"**
```bash
gcloud services enable aiplatform.googleapis.com
```

## Need Help?

1. Check [README.md](README.md) for troubleshooting
2. Verify your project ID: `gcloud config get-value project`
3. Check enabled APIs: `gcloud services list --enabled`

## Your First Try-On Checklist

- [ ] Authenticated with gcloud
- [ ] Enabled Vertex AI API
- [ ] Set GOOGLE_CLOUD_PROJECT environment variable
- [ ] Installed Python dependencies
- [ ] Added person image to `input_images/person/`
- [ ] Added clothing image to `input_images/clothing/`
- [ ] Run `python virtual_tryon.py`
- [ ] Check `output_images/` for results

Happy try-on! 🎉
