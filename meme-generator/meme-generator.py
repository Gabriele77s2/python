# pip install Pillow

from PIL import Image, ImageDraw, ImageFont

def create_meme(image_path, top_text, bottom_text, output_path):
    # Load the image
    img = Image.open(image_path)
    
    # Initialize the drawing context
    draw = ImageDraw.Draw(img)
    
    # Load a font (you might need to change the font file path)
    font = ImageFont.truetype("arial.ttf", 36)
    
    # Calculate text size and position
    text_width, text_height = draw.textsize(top_text, font)
    x = (img.width - text_width) / 2
    y = 10
    
    # Add top text
    draw.text((x, y), top_text, font=font, fill="white")
    
    # Calculate text size and position for bottom text
    text_width, text_height = draw.textsize(bottom_text, font)
    x = (img.width - text_width) / 2
    y = img.height - text_height - 10
    
    # Add bottom text
    draw.text((x, y), bottom_text, font=font, fill="white")
    
    # Save the meme
    img.save(output_path)

# Example usage
input_image_path = "input.jpg"
output_meme_path = "output_meme.jpg"
top_text = "Top Text"
bottom_text = "Bottom Text"

create_meme(input_image_path, top_text, bottom_text, output_meme_path)

# We load an image using Image.open.
# We use ImageDraw.Draw to create a drawing context on the image.
# We load a font using ImageFont.truetype. You might need to specify the correct font file path on your system.
# We calculate the text size and position for the top and bottom text.
# We add the top and bottom text to the image using draw.text.
# Finally, we save the meme with the added text.
