"""
Virtual Try-On Web UI
A simple, user-friendly interface for virtual try-on using Gradio
"""

import os
import sys
from datetime import datetime
from pathlib import Path
import gradio as gr
from PIL import Image

# Set environment variables
os.environ['GOOGLE_CLOUD_PROJECT'] = 'renderedfitsnew'
os.environ['GOOGLE_CLOUD_REGION'] = 'us-central1'

from virtual_tryon import VirtualTryOn
import config


# Initialize Virtual Try-On client
print("Initializing Virtual Try-On client...")
try:
    vto = VirtualTryOn(project_id='renderedfitsnew', location='us-central1')
    print("✅ Client initialized successfully!")
except Exception as e:
    print(f"❌ Error initializing client: {e}")
    print("\nPlease make sure you've authenticated:")
    print("  gcloud auth application-default login")
    vto = None


def virtual_tryon_single(person_image, clothing_image, num_images, safety_level, progress=gr.Progress()):
    """
    Perform virtual try-on with a single clothing item.

    Args:
        person_image: PIL Image of the person
        clothing_image: PIL Image of the clothing item
        num_images: Number of images to generate (1-4)
        safety_level: Safety filter level
        progress: Gradio progress tracker

    Returns:
        List of generated images or error message
    """
    if vto is None:
        return None, "❌ Virtual Try-On client not initialized. Please authenticate with Google Cloud."

    if person_image is None:
        return None, "❌ Please upload a person image."

    if clothing_image is None:
        return None, "❌ Please upload a clothing image."

    try:
        progress(0, desc="Preparing images...")

        # Save temporary files
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        temp_person = f"temp_person_{timestamp}.png"
        temp_clothing = f"temp_clothing_{timestamp}.png"

        person_image.save(temp_person)
        clothing_image.save(temp_clothing)

        progress(0.3, desc="Sending to Virtual Try-On API...")

        # Perform virtual try-on
        results = vto.try_on_single_item(
            person_image_path=temp_person,
            clothing_image_path=temp_clothing,
            number_of_images=num_images,
            safety_filter_level=safety_level
        )

        progress(0.8, desc="Loading results...")

        # Load generated images
        generated_images = []
        for result_path in results:
            img = Image.open(result_path)
            generated_images.append(img)

        # Clean up temp files
        os.remove(temp_person)
        os.remove(temp_clothing)

        progress(1.0, desc="Complete!")

        # Return first image and success message
        success_msg = f"✅ Success! Generated {len(generated_images)} image(s).\nSaved to: {results[0]}"

        if len(generated_images) == 1:
            return generated_images[0], success_msg
        else:
            # For multiple images, return as a gallery
            return generated_images, success_msg

    except Exception as e:
        # Clean up temp files if they exist
        try:
            if os.path.exists(temp_person):
                os.remove(temp_person)
            if os.path.exists(temp_clothing):
                os.remove(temp_clothing)
        except:
            pass

        error_msg = f"❌ Error: {str(e)}\n\n"
        error_msg += "Common issues:\n"
        error_msg += "1. Not authenticated - run: gcloud auth application-default login\n"
        error_msg += "2. API not enabled - run: gcloud services enable aiplatform.googleapis.com\n"
        error_msg += "3. Billing not enabled - check Google Cloud Console\n"
        error_msg += "4. Image format issues - ensure images are clear and well-lit"

        return None, error_msg


def virtual_tryon_multiple(person_image, clothing_images, safety_level, progress=gr.Progress()):
    """
    Perform virtual try-on with multiple clothing items sequentially.

    Args:
        person_image: PIL Image of the person
        clothing_images: List of PIL Images of clothing items
        safety_level: Safety filter level
        progress: Gradio progress tracker

    Returns:
        Final image or error message
    """
    if vto is None:
        return None, "❌ Virtual Try-On client not initialized. Please authenticate with Google Cloud."

    if person_image is None:
        return None, "❌ Please upload a person image."

    if not clothing_images or len(clothing_images) == 0:
        return None, "❌ Please upload at least one clothing image."

    try:
        progress(0, desc="Preparing images...")

        # Save temporary files
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        temp_person = f"temp_person_{timestamp}.png"
        person_image.save(temp_person)

        temp_clothing_paths = []
        for idx, clothing_img in enumerate(clothing_images):
            temp_path = f"temp_clothing_{timestamp}_{idx}.png"
            clothing_img.save(temp_path)
            temp_clothing_paths.append(temp_path)

        progress(0.3, desc=f"Processing {len(temp_clothing_paths)} items...")

        # Perform sequential try-on
        results = vto.try_on_multiple_items(
            person_image_path=temp_person,
            clothing_items=temp_clothing_paths,
            number_of_images=1,
            safety_filter_level=safety_level
        )

        progress(0.9, desc="Loading result...")

        # Load the final image (last result)
        final_image = Image.open(results[-1])

        # Clean up temp files
        os.remove(temp_person)
        for temp_path in temp_clothing_paths:
            os.remove(temp_path)

        progress(1.0, desc="Complete!")

        success_msg = f"✅ Success! Tried on {len(temp_clothing_paths)} items sequentially.\n"
        success_msg += f"Final result saved to: {results[-1]}"

        return final_image, success_msg

    except Exception as e:
        # Clean up temp files if they exist
        try:
            if os.path.exists(temp_person):
                os.remove(temp_person)
            for temp_path in temp_clothing_paths:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
        except:
            pass

        error_msg = f"❌ Error: {str(e)}\n\n"
        error_msg += "Common issues:\n"
        error_msg += "1. Not authenticated - run: gcloud auth application-default login\n"
        error_msg += "2. API not enabled - run: gcloud services enable aiplatform.googleapis.com\n"
        error_msg += "3. Billing not enabled - check Google Cloud Console"

        return None, error_msg


# Create Gradio interface
with gr.Blocks(title="Virtual Try-On", theme=gr.themes.Soft()) as app:

    gr.Markdown("""
    # 👔 Virtual Try-On with Google Vertex AI

    Upload a person image and clothing items to see how they look together!

    **Supported Clothing:** Tops, bottoms, dresses, footwear, and more.
    """)

    # Status indicator
    if vto is None:
        gr.Markdown("""
        ### ⚠️ Authentication Required

        Please authenticate with Google Cloud first:
        ```bash
        gcloud auth application-default login
        gcloud services enable aiplatform.googleapis.com --project=renderedfitsnew
        ```
        Then restart this app.
        """)
    else:
        gr.Markdown("""
        ### ✅ Connected to Vertex AI
        Project: **renderedfitsnew**
        """)

    with gr.Tabs():

        # Tab 1: Single Item Try-On
        with gr.Tab("Single Item Try-On"):
            gr.Markdown("### Try on one clothing item")

            with gr.Row():
                with gr.Column():
                    person_input = gr.Image(
                        label="Person Image",
                        type="pil",
                        sources=["upload", "webcam"],
                        height=400
                    )

                with gr.Column():
                    clothing_input = gr.Image(
                        label="Clothing Item",
                        type="pil",
                        sources=["upload"],
                        height=400
                    )

            with gr.Row():
                num_images = gr.Slider(
                    minimum=1,
                    maximum=4,
                    value=1,
                    step=1,
                    label="Number of Variations",
                    info="Generate multiple variations (1-4)"
                )

                safety_level = gr.Dropdown(
                    choices=[
                        "BLOCK_NONE",
                        "BLOCK_ONLY_HIGH",
                        "BLOCK_MEDIUM_AND_ABOVE",
                        "BLOCK_LOW_AND_ABOVE"
                    ],
                    value="BLOCK_LOW_AND_ABOVE",
                    label="Safety Filter Level",
                    info="Content filtering level"
                )

            generate_btn = gr.Button("✨ Generate Virtual Try-On", variant="primary", size="lg")

            with gr.Row():
                output_image = gr.Image(label="Result", height=500)

            status_text = gr.Textbox(label="Status", lines=3, max_lines=10)

            generate_btn.click(
                fn=virtual_tryon_single,
                inputs=[person_input, clothing_input, num_images, safety_level],
                outputs=[output_image, status_text]
            )

            gr.Markdown("""
            ### 💡 Tips for Best Results
            - Use clear, well-lit images
            - Person should be facing forward
            - Full body or relevant body part visible
            - Clothing items should be clearly visible
            - High-resolution images work best
            """)

        # Tab 2: Multiple Items Try-On
        with gr.Tab("Multiple Items Try-On"):
            gr.Markdown("### Try on multiple items sequentially (e.g., shirt → pants → shoes)")

            with gr.Row():
                with gr.Column():
                    person_input_multi = gr.Image(
                        label="Person Image",
                        type="pil",
                        sources=["upload", "webcam"],
                        height=400
                    )

                with gr.Column():
                    clothing_input_multi = gr.File(
                        label="Clothing Items (upload multiple)",
                        file_count="multiple",
                        file_types=["image"],
                        type="filepath"
                    )
                    gr.Markdown("*Upload 2-3 items. They will be applied in order.*")

            safety_level_multi = gr.Dropdown(
                choices=[
                    "BLOCK_NONE",
                    "BLOCK_ONLY_HIGH",
                    "BLOCK_MEDIUM_AND_ABOVE",
                    "BLOCK_LOW_AND_ABOVE"
                ],
                value="BLOCK_LOW_AND_ABOVE",
                label="Safety Filter Level"
            )

            generate_btn_multi = gr.Button("✨ Generate Sequential Try-On", variant="primary", size="lg")

            with gr.Row():
                output_image_multi = gr.Image(label="Final Result", height=500)

            status_text_multi = gr.Textbox(label="Status", lines=3, max_lines=10)

            def process_multiple_images(person_img, clothing_files, safety):
                if clothing_files is None or len(clothing_files) == 0:
                    return None, "Please upload clothing images"

                # Load images from file paths
                clothing_images = []
                for file_path in clothing_files:
                    img = Image.open(file_path)
                    clothing_images.append(img)

                return virtual_tryon_multiple(person_img, clothing_images, safety)

            generate_btn_multi.click(
                fn=process_multiple_images,
                inputs=[person_input_multi, clothing_input_multi, safety_level_multi],
                outputs=[output_image_multi, status_text_multi]
            )

            gr.Markdown("""
            ### 🔄 How Sequential Try-On Works
            1. First item is tried on the person
            2. Result becomes input for second item
            3. Process repeats for all items
            4. Best for complete outfits (top + bottom + shoes)
            """)

        # Tab 3: About & Help
        with gr.Tab("ℹ️ About & Help"):
            gr.Markdown("""
            ## Virtual Try-On using Google Vertex AI

            ### Supported Clothing Types
            - **Tops:** shirts, hoodies, sweaters, tank tops, blouses
            - **Bottoms:** pants, leggings, shorts, skirts
            - **Footwear:** sneakers, boots, sandals, flats, heels
            - **Dresses:** full dresses and gowns

            ### Cost Information
            - This uses Google's paid Vertex AI API
            - Typical cost: A few cents per image
            - Monitor usage in Google Cloud Console

            ### Troubleshooting

            **"Authentication Required" message:**
            ```bash
            gcloud auth application-default login
            ```

            **"API not enabled" error:**
            ```bash
            gcloud services enable aiplatform.googleapis.com --project=renderedfitsnew
            ```

            **Poor results:**
            - Use high-resolution images
            - Ensure good lighting
            - Person should face forward
            - Try adjusting safety filter level

            ### Project Information
            - **Project ID:** renderedfitsnew
            - **Region:** us-central1
            - **Model:** virtual-try-on-preview-08-04

            ### Useful Links
            - [Google Cloud Console](https://console.cloud.google.com/home/dashboard?project=renderedfitsnew)
            - [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs/generative-ai/image/virtual-try-on)
            - [Billing Dashboard](https://console.cloud.google.com/billing)

            ### Support
            For issues with this app, check the project documentation files.
            For Vertex AI issues, see Google Cloud documentation.
            """)

    gr.Markdown("""
    ---
    Made with ❤️ using [Gradio](https://gradio.app) and [Google Vertex AI](https://cloud.google.com/vertex-ai)
    """)


if __name__ == "__main__":
    print("\n" + "="*70)
    print("Starting Virtual Try-On Web Interface")
    print("="*70)
    print()

    if vto is None:
        print("⚠️  Authentication Required!")
        print()
        print("Run these commands first:")
        print("  1. gcloud auth application-default login")
        print("  2. gcloud services enable aiplatform.googleapis.com --project=renderedfitsnew")
        print()
        print("Then restart this app.")
        print()

    # Launch the app
    app.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False,
        show_error=True,
        quiet=False
    )
