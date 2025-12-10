"""
Example usage scripts for Virtual Try-On
Demonstrates different use cases and scenarios
"""

from virtual_tryon import VirtualTryOn
import config


def example_1_single_item():
    """Example 1: Try on a single clothing item."""
    print("\n" + "="*70)
    print("EXAMPLE 1: Single Clothing Item Try-On")
    print("="*70)

    vto = VirtualTryOn()

    result = vto.try_on_single_item(
        person_image_path="input_images/person/model.jpg",
        clothing_image_path="input_images/clothing/shirt.jpg",
        number_of_images=1,
        safety_filter_level="BLOCK_LOW_AND_ABOVE"
    )

    print(f"\nSuccess! Generated image saved to: {result[0]}")


def example_2_multiple_items():
    """Example 2: Try on multiple items sequentially."""
    print("\n" + "="*70)
    print("EXAMPLE 2: Multiple Items Try-On (Top + Bottom)")
    print("="*70)

    vto = VirtualTryOn()

    clothing_items = [
        "input_images/clothing/sweater.jpg",   # First: try on top
        "input_images/clothing/trousers.jpg"   # Then: try on bottom
    ]

    results = vto.try_on_multiple_items(
        person_image_path="input_images/person/model.jpg",
        clothing_items=clothing_items,
        number_of_images=1
    )

    print(f"\nSuccess! Generated {len(results)} images:")
    for idx, img_path in enumerate(results, 1):
        print(f"  {idx}. {img_path}")


def example_3_generate_multiple_variations():
    """Example 3: Generate multiple variations of the same try-on."""
    print("\n" + "="*70)
    print("EXAMPLE 3: Generate Multiple Variations")
    print("="*70)

    vto = VirtualTryOn()

    results = vto.try_on_single_item(
        person_image_path="input_images/person/model.jpg",
        clothing_image_path="input_images/clothing/dress.jpg",
        number_of_images=4,  # Generate 4 variations
        safety_filter_level="BLOCK_LOW_AND_ABOVE"
    )

    print(f"\nSuccess! Generated {len(results)} variations:")
    for idx, img_path in enumerate(results, 1):
        print(f"  {idx}. {img_path}")


def example_4_from_cloud_storage():
    """Example 4: Try on clothing from Google Cloud Storage."""
    print("\n" + "="*70)
    print("EXAMPLE 4: Try-On from Google Cloud Storage")
    print("="*70)

    vto = VirtualTryOn()

    # Example using the sample dress from the documentation
    gcs_uri = "gs://cloud-samples-data/generative-ai/image/dress.jpg"

    result = vto.try_on_from_gcs(
        person_image_path="input_images/person/model.jpg",
        clothing_gcs_uri=gcs_uri,
        number_of_images=1
    )

    print(f"\nSuccess! Generated image saved to: {result[0]}")


def example_5_complete_outfit():
    """Example 5: Try on a complete outfit (top, bottom, shoes)."""
    print("\n" + "="*70)
    print("EXAMPLE 5: Complete Outfit Try-On")
    print("="*70)

    vto = VirtualTryOn()

    outfit_items = [
        "input_images/clothing/shirt.jpg",
        "input_images/clothing/pants.jpg",
        "input_images/clothing/shoes.jpg"
    ]

    results = vto.try_on_multiple_items(
        person_image_path="input_images/person/model.jpg",
        clothing_items=outfit_items,
        output_prefix="output_images/complete_outfit"
    )

    print(f"\nSuccess! Generated complete outfit with {len(results)} images")


def example_6_custom_safety_filters():
    """Example 6: Using different safety filter levels."""
    print("\n" + "="*70)
    print("EXAMPLE 6: Custom Safety Filter Levels")
    print("="*70)

    vto = VirtualTryOn()

    # Less restrictive filter
    result = vto.try_on_single_item(
        person_image_path="input_images/person/model.jpg",
        clothing_image_path="input_images/clothing/shirt.jpg",
        number_of_images=1,
        safety_filter_level="BLOCK_ONLY_HIGH"  # Less restrictive
    )

    print(f"\nGenerated with BLOCK_ONLY_HIGH filter: {result[0]}")


def main():
    """Run all examples (comment out ones you don't want to run)."""

    print("\n" + "="*70)
    print("VIRTUAL TRY-ON EXAMPLES")
    print("="*70)
    print("\nNote: Make sure you have images in the input_images directory!")
    print("  - input_images/person/model.jpg (person image)")
    print("  - input_images/clothing/*.jpg (clothing items)")

    try:
        # Uncomment the examples you want to run:

        # example_1_single_item()
        # example_2_multiple_items()
        # example_3_generate_multiple_variations()
        # example_4_from_cloud_storage()
        # example_5_complete_outfit()
        # example_6_custom_safety_filters()

        print("\n" + "="*70)
        print("Uncomment the examples in example_usage.py to run them!")
        print("="*70)

    except FileNotFoundError as e:
        print(f"\nError: {e}")
        print("\nPlease make sure you have the required images in place.")
        print("See README.md for setup instructions.")
    except Exception as e:
        print(f"\nError: {e}")
        print("\nCheck your Google Cloud configuration and API access.")


if __name__ == "__main__":
    main()
