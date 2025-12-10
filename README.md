# Virtual Try-On with Google Vertex AI

A Python implementation for virtual try-on using Google's cutting-edge image generation models. Generate high-quality images of people virtually trying on clothing items.

## Features

- Single clothing item try-on
- Multiple clothing items try-on (sequential)
- Support for local images and Google Cloud Storage
- Configurable safety filters
- Generate 1-4 images per request
- Organized input/output directory structure

## Supported Clothing Types

- **Tops**: shirts, hoodies, sweaters, tank tops, blouses
- **Bottoms**: pants, leggings, shorts, skirts
- **Footwear**: sneakers, boots, sandals, flats, heels, formal shoes

## Prerequisites

1. **Google Cloud Account** with billing enabled
2. **Google Cloud Project** with Vertex AI API enabled
3. **Python 3.8+** installed on your system
4. **gcloud CLI** installed and configured

## Setup Guide

### Step 1: Install Google Cloud CLI

If you haven't already, install the gcloud CLI:

**macOS:**
```bash
brew install google-cloud-sdk
```

**Linux/Windows:**
Follow the instructions at: https://cloud.google.com/sdk/docs/install

### Step 2: Authenticate with Google Cloud

```bash
# Login to your Google Cloud account
gcloud auth login

# Set up application default credentials
gcloud auth application-default login

# Set your project ID (replace with your actual project ID)
gcloud config set project YOUR_PROJECT_ID
```

### Step 3: Enable Required APIs

```bash
# Enable Vertex AI API
gcloud services enable aiplatform.googleapis.com

# Enable Cloud Storage API (if using GCS)
gcloud services enable storage-api.googleapis.com
```

### Step 4: Set Environment Variables

```bash
# Set your Google Cloud project ID
export GOOGLE_CLOUD_PROJECT="your-project-id"

# Optional: Set region (default is us-central1)
export GOOGLE_CLOUD_REGION="us-central1"
```

To make these permanent, add them to your `~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`:

```bash
echo 'export GOOGLE_CLOUD_PROJECT="your-project-id"' >> ~/.zshrc
echo 'export GOOGLE_CLOUD_REGION="us-central1"' >> ~/.zshrc
source ~/.zshrc
```

### Step 5: Install Python Dependencies

```bash
# Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### Step 6: Prepare Your Images

Create the directory structure and add your images:

```bash
# Directories are created automatically, but you can create them manually:
mkdir -p input_images/person
mkdir -p input_images/clothing
mkdir -p output_images
```

Add your images:
- Person images go in: `input_images/person/`
- Clothing images go in: `input_images/clothing/`

**Image Requirements:**
- Person images should show the full body or the relevant body part
- Clothing images should be clear with good lighting
- Supported formats: JPEG, PNG
- Recommended: High-resolution images for best results

## Usage

### Option 1: Run the Demo Script

The main script includes examples of single and multiple item try-ons:

```bash
python virtual_tryon.py
```

### Option 2: Use as a Python Module

```python
from virtual_tryon import VirtualTryOn

# Initialize
vto = VirtualTryOn()

# Single item try-on
result = vto.try_on_single_item(
    person_image_path="input_images/person/model.jpg",
    clothing_image_path="input_images/clothing/shirt.jpg",
    number_of_images=1
)

# Multiple items try-on (e.g., top then bottom)
results = vto.try_on_multiple_items(
    person_image_path="input_images/person/model.jpg",
    clothing_items=[
        "input_images/clothing/top.jpg",
        "input_images/clothing/bottom.jpg"
    ]
)

# Try-on from Google Cloud Storage
result = vto.try_on_from_gcs(
    person_image_path="input_images/person/model.jpg",
    clothing_gcs_uri="gs://your-bucket/clothing/dress.jpg"
)
```

### Option 3: Interactive Python Script

```python
python3 -c "
from virtual_tryon import VirtualTryOn

vto = VirtualTryOn()
result = vto.try_on_single_item(
    person_image_path='input_images/person/model.jpg',
    clothing_image_path='input_images/clothing/shirt.jpg'
)
print(f'Generated: {result[0]}')
"
```

## Configuration

Edit [config.py](config.py) to customize:

- Model versions
- Default output format
- Safety filter levels
- Directory paths
- Number of images to generate

Available safety filter levels:
- `BLOCK_NONE` - No filtering
- `BLOCK_ONLY_HIGH` - Block only high-risk content
- `BLOCK_MEDIUM_AND_ABOVE` - Block medium and high-risk content
- `BLOCK_LOW_AND_ABOVE` - Most strict filtering (default)

## Project Structure

```
Vertex/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── config.py                 # Configuration settings
├── virtual_tryon.py         # Main virtual try-on implementation
├── .env.example             # Example environment variables
├── input_images/
│   ├── person/              # Place person images here
│   └── clothing/            # Place clothing images here
└── output_images/           # Generated images saved here
```

## Troubleshooting

### Error: "Project ID not set"

Make sure you've set the environment variable:
```bash
export GOOGLE_CLOUD_PROJECT="your-project-id"
```

### Error: "Permission denied" or "API not enabled"

Enable the Vertex AI API:
```bash
gcloud services enable aiplatform.googleapis.com
```

### Error: "Authentication failed"

Re-authenticate:
```bash
gcloud auth application-default login
```

### Error: "Quota exceeded"

Check your quotas in the Google Cloud Console:
https://console.cloud.google.com/iam-admin/quotas

### Images not generating properly

- Ensure person images show the full body clearly
- Use high-resolution clothing images
- Check that file paths are correct
- Try adjusting the safety filter level

## Pricing

Virtual Try-On uses Vertex AI's pricing model. Check current pricing at:
https://cloud.google.com/vertex-ai/pricing

As of 2025, expect costs per image generation. Monitor your usage in the Google Cloud Console.

## Quotas and Limits

- Images per request: 1-4
- Maximum image size: Check Vertex AI documentation for current limits
- API rate limits: Apply based on your project quota

View your quotas:
```bash
gcloud compute project-info describe --project=YOUR_PROJECT_ID
```

## Best Practices

1. **Image Quality**: Use high-resolution images for best results
2. **Person Positioning**: Full-body shots work best for complete outfits
3. **Lighting**: Well-lit images produce better results
4. **Background**: Clean backgrounds help the model focus on the subject
5. **Sequential Try-On**: When trying multiple items, try tops before bottoms
6. **Cost Management**: Generate 1 image first, then increase if needed
7. **Safety Filters**: Start with `BLOCK_LOW_AND_ABOVE` for production use

## Additional Resources

- [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
- [Virtual Try-On API Reference](https://cloud.google.com/vertex-ai/docs/generative-ai/image/virtual-try-on)
- [Google Gen AI SDK](https://github.com/googleapis/python-genai)

## Support

For issues with:
- **This code**: Open an issue in this repository
- **Vertex AI**: Check [Google Cloud Support](https://cloud.google.com/support)
- **API Questions**: See [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)

## License

This project is provided as-is for demonstration purposes.
