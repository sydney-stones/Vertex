"""
Virtual Try-On Web UI
For local execution and testing.
"""

import os
import sys
from datetime import datetime
from pathlib import Path
import gradio as gr
from PIL import Image

# --- Authentication Check ---
# This local app relies on Application Default Credentials.
# Run `gcloud auth application-default login` if you see auth errors.
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")

# --- Output Directory ---
OUTPUT_DIR = Path("output_images")
OUTPUT_DIR.mkdir(exist_ok=True)

def get_project_id():
    if not PROJECT_ID:
        raise gr.Error("GOOGLE_CLOUD_PROJECT environment variable not set!")
    return PROJECT_ID

from virtual_tryon import VirtualTryOn
import config


# Initialize Virtual Try-On client
print("Initializing Virtual Try-On client...")
try:
    vto = VirtualTryOn(project_id=get_project_id(), location='us-central1')
    print("✅ Client initialized successfully!")
    AUTH_SUCCESS = True
except Exception as e:
    print(f"❌ Error initializing client: {e}")
    vto = None
    AUTH_SUCCESS = False


def virtual_tryon_single(person_image, clothing_image, num_images, safety_level, progress=gr.Progress()):
    """Perform virtual try-on with a single clothing item."""
    if not AUTH_SUCCESS or vto is None:
        raise gr.Error("Virtual Try-On client failed to initialize. Check authentication.")

    if person_image is None:
        return None, "❌ Please upload a person image."

    if clothing_image is None:
        return None, "❌ Please upload a clothing image."

    try:
        progress(0, desc="Preparing images...")

        # Save temporary files
        temp_dir = Path("/tmp/vto_ui")
        temp_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        temp_person = temp_dir / f"temp_person_{timestamp}.png"
        temp_clothing = temp_dir / f"temp_clothing_{timestamp}.png"

        person_image.save(str(temp_person))
        clothing_image.save(str(temp_clothing))

        progress(0.3, desc="Sending to Virtual Try-On API...")

        # Perform virtual try-on
        results = vto.try_on_single_item(
            person_image_path=temp_person,
            clothing_image_path=temp_clothing,
            # The API generates a fixed number of images, but we can save them.
            # This parameter is illustrative for the UI.
            safety_filter_level=safety_level
        )

        progress(0.8, desc="Loading results...")

        # Load generated images
        generated_images = []
        for result_path in results:
            try:
                img = Image.open(result_path)
                # Save to the local output directory
                save_path = OUTPUT_DIR / Path(result_path).name
                img.save(save_path)
                generated_images.append(img)
            except Exception as img_e:
                print(f"Error processing result image: {img_e}")

        # Clean up temp files
        try:
            os.remove(temp_person)
            os.remove(temp_clothing)
        except OSError:
            pass

        progress(1.0, desc="Complete!")
        success_msg = f"✅ Success! Saved {len(generated_images)} image(s) to `output_images/`."

        if len(generated_images) == 1:
            return generated_images[0], success_msg
        else:
            return generated_images, success_msg

    except Exception as e:
        error_msg = f"❌ An error occurred: {str(e)}"
        if "permission" in str(e).lower() or "credentials" in str(e).lower():
            error_msg += "\n\n**Authentication Error:** Please run `gcloud auth application-default login` in your terminal and restart the app."
        raise gr.Error(error_msg)


def virtual_tryon_multiple(person_image, clothing_images, safety_level, progress=gr.Progress()):
    """Perform virtual try-on with multiple clothing items sequentially."""
    if not AUTH_SUCCESS or vto is None:
        raise gr.Error("Virtual Try-On client failed to initialize. Check authentication.")

    if person_image is None:
        return None, "❌ Please upload a person image."

    if not clothing_images or len(clothing_images) == 0:
        return None, "❌ Please upload at least one clothing image."

    try:
        progress(0, desc="Preparing images...")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        temp_dir = Path("/tmp/vto_ui")
        temp_dir.mkdir(exist_ok=True)
        temp_person = temp_dir / f"temp_person_multi_{timestamp}.png"
        person_image.save(temp_person)

        temp_clothing_paths = []
        for idx, clothing_img in enumerate(clothing_images):
            temp_path = temp_dir / f"temp_clothing_multi_{timestamp}_{idx}.png"
            clothing_img.save(temp_path)
            temp_clothing_paths.append(str(temp_path))

        progress(0.3, desc=f"Processing {len(temp_clothing_paths)} items...")

        results = vto.try_on_multiple_items(
            person_image_path=temp_person,
            clothing_items=temp_clothing_paths,
            number_of_images=1,
            safety_filter_level=safety_level
        )

        progress(0.9, desc="Loading result...")

        final_result_path = results[-1]
        final_image = Image.open(final_result_path)
        save_path = OUTPUT_DIR / Path(final_result_path).name
        final_image.save(save_path)

        # Clean up temp files
        try:
            os.remove(temp_person)
            for temp_path in temp_clothing_paths:
                os.remove(temp_path)
        except OSError:
            pass

        progress(1.0, desc="Complete!")
        success_msg = f"✅ Success! Final image saved to `output_images/`."
        return final_image, success_msg

    except Exception as e:
        error_msg = f"❌ An error occurred: {str(e)}"
        raise gr.Error(error_msg)


# Create Gradio interface
with gr.Blocks(title="Virtual Try-On", theme=gr.themes.Soft()) as app:

    gr.Markdown("""
    # 👔 Virtual Try-On with Google Vertex AI

    Upload a person image and clothing items to see how they look together!

    **Supported Clothing:** Tops, bottoms, dresses, footwear, and more.
    """)

    # Status indicator
    if not AUTH_SUCCESS:
        gr.Markdown(
            "### ⚠️ Authentication Error\n"
            "Could not connect to Google Cloud. Please run `gcloud auth application-default login` "
            "in your terminal and restart the app."
        )
    else:
        gr.Markdown(f"### ✅ Connected to Vertex AI in project: `{PROJECT_ID}`")

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
                    label="Safety Filter Level"
                )

            generate_btn = gr.Button("✨ Generate Virtual Try-On", variant="primary", size="lg")

            with gr.Row():
                # Use Gallery to support multiple output images
                output_gallery = gr.Gallery(
                    label="Result(s)",
                    height=500,
                )

            status_text = gr.Textbox(label="Status", lines=3, max_lines=10)

            generate_btn.click(
                fn=virtual_tryon_single,
                inputs=[person_input, clothing_input, num_images, safety_level],
                outputs=[output_gallery, status_text]
            )

            gr.Markdown("""
            ### 💡 Tips for Best Results
            - Use clear, well-lit images
            - Person should be facing forward
            - Full body or relevant body part visible
            - High-resolution images work best
            """)

        # Tab 2: Multiple Items Try-On
        with gr.Tab("Multiple Items Try-On"):
            gr.Markdown("### Try on multiple items sequentially")

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
                        file_types=["image", ".png", ".jpg", ".jpeg"],
                        type="filepath"
                    )
                    gr.Markdown("*Upload 2-3 items in order*")

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

            output_image_multi = gr.Image(label="Final Result", height=500)
            status_text_multi = gr.Textbox(label="Status", lines=3, max_lines=10)

            def process_multiple_images(person_img, clothing_files, safety):
                if clothing_files is None or len(clothing_files) == 0:
                    return None, "Please upload clothing images"

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

        # Tab 3: About
        with gr.Tab("ℹ️ About"):
            gr.Markdown("""
            ## Virtual Try-On using Google Vertex AI

            ### Supported Clothing Types
            - **Tops:** shirts, hoodies, sweaters, tank tops, blouses
            - **Bottoms:** pants, leggings, shorts, skirts
            - **Footwear:** sneakers, boots, sandals, flats, heels
            - **Dresses:** full dresses and gowns

            ### How It Works
            1. Upload a person image
            2. Upload clothing item(s)
            3. Click generate
            4. Wait ~15-30 seconds
            5. View your result!

            ### Tips
            - Use high-resolution images (1024x1024+)
            - Ensure good lighting
            - Person should face forward
            - Clear clothing images work best

            ### Technology
            Powered by Google's Vertex AI Virtual Try-On model.
            """)

    gr.Markdown("""
    ---
    Made with Gradio and Google Vertex AI
    """)


if __name__ == "__main__":
    app.launch(
        server_name="0.0.0.0",
        server_port=7861, # Using a different port to avoid conflict
        share=False
    )
