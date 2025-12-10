"""
Virtual Try-On using Google Vertex AI
Demonstrates how to use Google's Virtual Try-On model to generate images of people wearing clothing items.
"""

import sys
from pathlib import Path
from datetime import datetime
from typing import Optional

from google import genai
from google.genai.types import (
    Image,
    ProductImage,
    RecontextImageConfig,
    RecontextImageSource,
)
from PIL import Image as PIL_Image
from PIL import ImageOps as PIL_ImageOps

import config


class VirtualTryOn:
    """Virtual Try-On class for managing try-on operations."""

    def __init__(self, project_id: Optional[str] = None, location: Optional[str] = None):
        """Initialize the Virtual Try-On client.

        Args:
            project_id: Google Cloud Project ID
            location: Google Cloud region (default: us-central1)
        """
        self.project_id = project_id or config.PROJECT_ID
        self.location = location or config.LOCATION

        if not self.project_id:
            raise ValueError(
                "Project ID not set. Please set GOOGLE_CLOUD_PROJECT environment variable "
                "or pass project_id parameter."
            )

        print(f"Initializing Virtual Try-On client...")
        print(f"Project: {self.project_id}")
        print(f"Location: {self.location}")

        self.client = genai.Client(
            vertexai=True,
            project=self.project_id,
            location=self.location
        )
        print("Client initialized successfully!\n")

    def try_on_single_item(
        self,
        person_image_path: str,
        clothing_image_path: str,
        output_path: Optional[str] = None,
        number_of_images: int = 1,
        safety_filter_level: str = "BLOCK_LOW_AND_ABOVE"
    ) -> list:
        """Try on a single clothing item.

        Args:
            person_image_path: Path to the person image
            clothing_image_path: Path to the clothing item image
            output_path: Optional output path for the generated image
            number_of_images: Number of images to generate (1-4)
            safety_filter_level: Safety filter level

        Returns:
            List of generated images
        """
        print(f"Processing try-on:")
        print(f"  Person: {person_image_path}")
        print(f"  Clothing: {clothing_image_path}")

        response = self.client.models.recontext_image(
            model=config.VIRTUAL_TRY_ON_MODEL,
            source=RecontextImageSource(
                person_image=Image.from_file(location=person_image_path),
                product_images=[
                    ProductImage(product_image=Image.from_file(location=clothing_image_path))
                ],
            ),
            config=RecontextImageConfig(
                output_mime_type=config.DEFAULT_OUTPUT_FORMAT,
                number_of_images=number_of_images,
                safety_filter_level=safety_filter_level,
            ),
        )

        # Save the generated images
        generated_images = []
        for idx, generated_image in enumerate(response.generated_images):
            if output_path:
                save_path = output_path
            else:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                save_path = str(config.OUTPUT_DIR / f"tryon_{timestamp}_{idx}.jpeg")

            generated_image.image.save(save_path)
            generated_images.append(save_path)
            print(f"  Saved: {save_path}")

        return generated_images

    def try_on_multiple_items(
        self,
        person_image_path: str,
        clothing_items: list[str],
        output_prefix: Optional[str] = None,
        number_of_images: int = 1,
        safety_filter_level: str = "BLOCK_LOW_AND_ABOVE"
    ) -> list:
        """Try on multiple clothing items sequentially.

        Args:
            person_image_path: Path to the initial person image
            clothing_items: List of paths to clothing item images
            output_prefix: Optional prefix for output files
            number_of_images: Number of images to generate per item
            safety_filter_level: Safety filter level

        Returns:
            List of paths to generated images
        """
        print(f"\n{'='*60}")
        print(f"Starting multi-item try-on with {len(clothing_items)} items")
        print(f"{'='*60}\n")

        current_person_image = person_image_path
        all_outputs = []

        for idx, clothing_item in enumerate(clothing_items, 1):
            print(f"[{idx}/{len(clothing_items)}] Trying on: {Path(clothing_item).name}")

            if output_prefix:
                output_path = f"{output_prefix}_item{idx}.jpeg"
            else:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = str(config.OUTPUT_DIR / f"multi_tryon_{timestamp}_item{idx}.jpeg")

            outputs = self.try_on_single_item(
                person_image_path=current_person_image,
                clothing_image_path=clothing_item,
                output_path=output_path,
                number_of_images=number_of_images,
                safety_filter_level=safety_filter_level
            )

            # Use the output of this try-on as input for the next one
            current_person_image = outputs[0]
            all_outputs.extend(outputs)
            print()

        print(f"{'='*60}")
        print(f"Multi-item try-on complete! Generated {len(all_outputs)} images")
        print(f"{'='*60}\n")

        return all_outputs

    def try_on_from_gcs(
        self,
        person_image_path: str,
        clothing_gcs_uri: str,
        output_path: Optional[str] = None,
        number_of_images: int = 1,
        safety_filter_level: str = "BLOCK_LOW_AND_ABOVE"
    ) -> list:
        """Try on a clothing item from Google Cloud Storage.

        Args:
            person_image_path: Path to the person image (local or GCS)
            clothing_gcs_uri: GCS URI of the clothing item (gs://...)
            output_path: Optional output path for the generated image
            number_of_images: Number of images to generate (1-4)
            safety_filter_level: Safety filter level

        Returns:
            List of generated images
        """
        print(f"Processing try-on from GCS:")
        print(f"  Person: {person_image_path}")
        print(f"  Clothing GCS URI: {clothing_gcs_uri}")

        # Load person image (could be local or GCS)
        if person_image_path.startswith("gs://"):
            person_img = Image(gcs_uri=person_image_path)
        else:
            person_img = Image.from_file(location=person_image_path)

        response = self.client.models.recontext_image(
            model=config.VIRTUAL_TRY_ON_MODEL,
            source=RecontextImageSource(
                person_image=person_img,
                product_images=[
                    ProductImage(product_image=Image(gcs_uri=clothing_gcs_uri))
                ],
            ),
            config=RecontextImageConfig(
                output_mime_type=config.DEFAULT_OUTPUT_FORMAT,
                number_of_images=number_of_images,
                safety_filter_level=safety_filter_level,
            ),
        )

        # Save the generated images
        generated_images = []
        for idx, generated_image in enumerate(response.generated_images):
            if output_path:
                save_path = output_path
            else:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                save_path = str(config.OUTPUT_DIR / f"tryon_gcs_{timestamp}_{idx}.jpeg")

            generated_image.image.save(save_path)
            generated_images.append(save_path)
            print(f"  Saved: {save_path}")

        return generated_images


def main():
    """Main function demonstrating Virtual Try-On usage."""

    # Initialize Virtual Try-On
    try:
        vto = VirtualTryOn()
    except ValueError as e:
        print(f"Error: {e}")
        print("\nPlease set your Google Cloud Project ID:")
        print("  export GOOGLE_CLOUD_PROJECT='your-project-id'")
        sys.exit(1)

    # Example 1: Single item try-on
    print("\n" + "="*60)
    print("EXAMPLE 1: Single Item Try-On")
    print("="*60)

    person_img = config.INPUT_DIR / "person" / "model.jpg"
    clothing_img = config.INPUT_DIR / "clothing" / "shirt.jpg"

    if person_img.exists() and clothing_img.exists():
        result = vto.try_on_single_item(
            person_image_path=str(person_img),
            clothing_image_path=str(clothing_img),
            number_of_images=1
        )
        print(f"\nGenerated image: {result[0]}")
    else:
        print(f"\nSkipping - Please add images to:")
        print(f"  Person: {person_img}")
        print(f"  Clothing: {clothing_img}")

    # Example 2: Multiple items try-on
    print("\n" + "="*60)
    print("EXAMPLE 2: Multiple Items Try-On")
    print("="*60)

    top_img = config.INPUT_DIR / "clothing" / "top.jpg"
    bottom_img = config.INPUT_DIR / "clothing" / "bottom.jpg"

    if person_img.exists() and top_img.exists() and bottom_img.exists():
        results = vto.try_on_multiple_items(
            person_image_path=str(person_img),
            clothing_items=[str(top_img), str(bottom_img)],
            number_of_images=1
        )
        print(f"\nGenerated {len(results)} images")
        for img_path in results:
            print(f"  - {img_path}")
    else:
        print(f"\nSkipping - Please add images to:")
        print(f"  Person: {person_img}")
        print(f"  Top: {top_img}")
        print(f"  Bottom: {bottom_img}")

    print("\n" + "="*60)
    print("Examples complete!")
    print("="*60)


if __name__ == "__main__":
    main()
