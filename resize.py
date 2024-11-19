from PIL import Image

# List of screenshots to resize
screenshots = [
    "assets/screenshot-0.png",
    "assets/screenshot-1.png",
    "assets/screenshot-2.png",
    "assets/screenshot-3.png"
]

# Resize each screenshot
for screenshot in screenshots:
    img = Image.open(screenshot)
    img = img.resize((1024, 768))  # Resize to 1024x768
    img.save(screenshot)  # Save the resized image back to the same file
