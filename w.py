import os
from PIL import Image, ImageDraw, ImageFont

# Directories
ITEMS_DIR = '~/Items/ob'
WATERMARK_DIR = '~/watermark'

# Ensure the watermark directory exists
os.makedirs(WATERMARK_DIR, exist_ok=True)

def add_watermark_to_image(img_path, output_path, watermark_text="@PikaApis"):
    try:
        # Open the image
        img = Image.open(img_path)

        # Add watermark
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()  # Use default font

        # Calculate text size using textbbox
        text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

        # Calculate the center position
        position = ((img.width - text_width) // 2, (img.height - text_height) // 2)

        # Draw the watermark text at the center
        draw.text(position, watermark_text, (255, 255, 255), font=font)

        # Save the watermarked image
        img.save(output_path, format="PNG")
    except Exception as e:
        print(f"Error adding watermark to {img_path}: {e}")

def process_all_images():
    # Get a list of all images in the ITEMS_DIR
    images = [f for f in os.listdir(ITEMS_DIR) if f.endswith('.png')]

    if not images:
        print("No images found in the source directory.")
        return

    print(f"Processing {len(images)} images...")
    for img_name in images:
        img_path = os.path.join(ITEMS_DIR, img_name)
        output_path = os.path.join(WATERMARK_DIR, img_name)

        # Add watermark to each image
        add_watermark_to_image(img_path, output_path)
        print(f"Watermarked {img_name} and saved to {output_path}")

    print("All images processed successfully.")

# Run the script
process_all_images()
