import os
from pathlib import Path

# Google Cloud Configuration
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT", "")
LOCATION = os.environ.get("GOOGLE_CLOUD_REGION", "us-central1")

# Model Configuration
VIRTUAL_TRY_ON_MODEL = "virtual-try-on-preview-08-04"
IMAGE_GENERATION_MODEL = "imagen-4.0-generate-001"

# Image Settings
DEFAULT_OUTPUT_FORMAT = "image/jpeg"
DEFAULT_NUMBER_OF_IMAGES = 1
DEFAULT_SAFETY_LEVEL = "BLOCK_LOW_AND_ABOVE"

# Directory Configuration
BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "input_images"
OUTPUT_DIR = BASE_DIR / "output_images"

# Create directories if they don't exist
INPUT_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)
(INPUT_DIR / "person").mkdir(exist_ok=True)
(INPUT_DIR / "clothing").mkdir(exist_ok=True)
