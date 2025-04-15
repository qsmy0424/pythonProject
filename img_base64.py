from PIL import Image
import io
import base64


def convert_image_to_webp_base64(input_image_path):
    try:
        with Image.open(input_image_path) as img:
            byte_arr = io.BytesIO()
            img.save(byte_arr, format="webp")
            byte_arr = byte_arr.getvalue()
            base64_str = base64.b64encode(byte_arr).decode("utf-8")
            return base64_str
    except IOError:
        print(f"Error: Unable to open or convert the image {input_image_path}")
        return None


base64_image = convert_image_to_webp_base64("C:\\Users\\qsmy\\Desktop\\123.jpg")

print(base64_image)
