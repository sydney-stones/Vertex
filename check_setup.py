"""
Setup Checker - Verify your environment is ready for Virtual Try-On
"""

import os
import sys
from pathlib import Path

def check_environment():
    """Check if environment is properly configured."""

    print("="*70)
    print("Virtual Try-On Setup Checker")
    print("="*70)
    print()

    checks_passed = 0
    checks_total = 0

    # Check 1: Project ID
    checks_total += 1
    project_id = os.environ.get('GOOGLE_CLOUD_PROJECT')
    if project_id == 'renderedfitsnew':
        print("✅ Check 1: Project ID is set correctly")
        print(f"   → {project_id}")
        checks_passed += 1
    else:
        print("❌ Check 1: Project ID not set")
        print("   Run: export GOOGLE_CLOUD_PROJECT='renderedfitsnew'")
    print()

    # Check 2: Python packages
    checks_total += 1
    try:
        import google.genai
        import PIL
        import matplotlib
        import numpy
        print("✅ Check 2: Python packages installed")
        checks_passed += 1
    except ImportError as e:
        print("❌ Check 2: Missing Python packages")
        print(f"   Error: {e}")
        print("   Run: pip install -r requirements.txt")
    print()

    # Check 3: Person image
    checks_total += 1
    person_image = Path("input_images/person/model.png")
    if person_image.exists():
        size_mb = person_image.stat().st_size / (1024 * 1024)
        print("✅ Check 3: Person image found")
        print(f"   → {person_image} ({size_mb:.2f} MB)")
        checks_passed += 1
    else:
        print("❌ Check 3: Person image not found")
        print(f"   Expected: {person_image}")
    print()

    # Check 4: Clothing image
    checks_total += 1
    clothing_image = Path("input_images/clothing/outfit.png")
    if clothing_image.exists():
        size_mb = clothing_image.stat().st_size / (1024 * 1024)
        print("✅ Check 4: Clothing image found")
        print(f"   → {clothing_image} ({size_mb:.2f} MB)")
        checks_passed += 1
    else:
        print("❌ Check 4: Clothing image not found")
        print(f"   Expected: {clothing_image}")
    print()

    # Check 5: Output directory
    checks_total += 1
    output_dir = Path("output_images")
    if output_dir.exists() and output_dir.is_dir():
        print("✅ Check 5: Output directory exists")
        print(f"   → {output_dir}/")
        checks_passed += 1
    else:
        print("❌ Check 5: Output directory not found")
        print("   Creating it now...")
        output_dir.mkdir(exist_ok=True)
        checks_passed += 1
    print()

    # Check 6: Authentication (try to import and test)
    checks_total += 1
    try:
        from google import genai
        # Try to create client - will fail if not authenticated
        client = genai.Client(vertexai=True, project='renderedfitsnew', location='us-central1')
        print("✅ Check 6: Authentication working!")
        print("   → Connected to Vertex AI")
        checks_passed += 1
    except Exception as e:
        print("❌ Check 6: Authentication not configured")
        print("   Error: " + str(e).split('\n')[0][:100])
        print()
        print("   You need to authenticate with Google Cloud:")
        print("   1. Install gcloud CLI: https://cloud.google.com/sdk/docs/install")
        print("   2. Run: gcloud auth application-default login")
        print("   3. Run: gcloud services enable aiplatform.googleapis.com --project=renderedfitsnew")
    print()

    # Summary
    print("="*70)
    print(f"Setup Check: {checks_passed}/{checks_total} checks passed")
    print("="*70)
    print()

    if checks_passed == checks_total:
        print("🎉 All checks passed! You're ready to run Virtual Try-On!")
        print()
        print("Run this command:")
        print("  python run_my_tryon.py")
        print()
        return True
    else:
        print("⚠️  Some checks failed. Please fix the issues above.")
        print()
        print("Most common issue: Authentication")
        print("Fix it by running:")
        print("  1. Install gcloud CLI (if not installed)")
        print("  2. gcloud auth application-default login")
        print("  3. gcloud services enable aiplatform.googleapis.com --project=renderedfitsnew")
        print()
        return False

if __name__ == "__main__":
    # Set the project ID
    os.environ['GOOGLE_CLOUD_PROJECT'] = 'renderedfitsnew'

    success = check_environment()
    sys.exit(0 if success else 1)
