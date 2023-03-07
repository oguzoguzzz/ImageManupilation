from PIL import Image, ImageFilter

def resize_image(image_path,width,height):
    """ Resize an image to the specified width and height."""
    with Image.open(image_path) as img:
        resized = img.resize((width,height))
        resized.save('resized.jpg')

def apply_filter(image_path,filter_name):
    """ Apply a filter to an image."""
    with Image.open(image_path) as img:
        filtered = img.filter(filter_name)
        filtered.save('filtered.jpg')

# Usage
image_path ='sassu.png'
resize_image(image_path, 640x480)
apply_filter(image_path, ImageFilter.SHARPEN)


