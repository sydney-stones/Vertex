"""
Custom Virtual Try-On script for your images
Uses model.png and outfit.png
"""

import os
import sys

# Set environment variables
os.environ['GOOGLE_CLOUD_PROJECT'] = 'renderedfitsnew'
os.environ['GOOGLE_CLOUD_REGION'] = 'us-central1'

from virtual_tryon import VirtualTryOn
from pathlib import Path

def main():
    print("="*70)
    print("Virtual Try-On Demo - renderedfitsnew")
    print("="*70)
    print()

    # Initialize Virtual Try-On
    print("Initializing Virtual Try-On client...")
    try:
        vto = VirtualTryOn(project_id='renderedfitsnew', location='us-central1')
    except Exception as e:
        print(f"\n❌ Error initializing client: {e}")
        print("\nPlease make sure you've run:")
        print("  gcloud auth application-default login")
        print("  gcloud services enable aiplatform.googleapis.com --project=renderedfitsnew")
        sys.exit(1)

    # Your images
    person_image = "input_images/person/model.png"
    clothing_image = "input_images/clothing/outfit.png"

    # Verify images exist
    if not Path(person_image).exists():
        print(f"❌ Person image not found: {person_image}")
        sys.exit(1)

    if not Path(clothing_image).exists():
        print(f"❌ Clothing image not found: {clothing_image}")
        sys.exit(1)

    print(f"✅ Found person image: {person_image}")
    print(f"✅ Found clothing image: {clothing_image}")
    print()

    # Run virtual try-on
    print("="*70)
    print("Starting Virtual Try-On...")
    print("="*70)
    print()

    try:
        result = vto.try_on_single_item(
            person_image_path=person_image,
            clothing_image_path=clothing_image,
            number_of_images=1,
            safety_filter_level="BLOCK_LOW_AND_ABOVE"
        )

        print()
        print("="*70)
        print("✅ SUCCESS! Virtual Try-On Complete!")
        print("="*70)
        print()
        print(f"Generated image saved to:")
        print(f"  {result[0]}")
        print()
        print("You can view the image in the output_images/ folder!")
        print()

    except Exception as e:
        print()
        print("="*70)
        print("❌ Error during virtual try-on")
        print("="*70)
        print()
        print(f"Error: {e}")
        print()
        print("Common issues:")
        print("  1. Not authenticated - run: gcloud auth application-default login")
        print("  2. API not enabled - run: gcloud services enable aiplatform.googleapis.com")
        print("  3. Billing not enabled - check: https://console.cloud.google.com/billing")
        print("  4. Image format issues - ensure images are JPEG or PNG")
        print()
        sys.exit(1)

if __name__ == "__main__":
    main()
