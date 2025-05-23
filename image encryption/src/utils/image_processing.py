from PIL import Image

def load_image(image_path: str) -> Image:
    return Image.open(image_path)

def save_image(image: Image, output_path: str) -> None:
    image.save(output_path)