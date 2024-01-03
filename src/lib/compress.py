from PIL import Image
import os


def resize_images_to_1080p(input_folder):
    output_folder = os.path.join(input_folder, "output")
    os.makedirs(output_folder, exist_ok=True)

    image_files = []
    for file in os.listdir(input_folder):
        if file.endswith(".jpg"):
            image_files.append(file)

    for file_name in image_files:
        try:
            img = Image.open(os.path.join(input_folder, file_name))
            width, height = img.size

            # Define 1080p resolution
            target_width = 1920  # 1080p width
            target_height = 1080  # 1080p height

            # Resize only if image resolution is larger than 1080p
            if width > target_width or height > target_height:
                img.thumbnail((target_width, target_height), Image.LANCZOS)
                output_path = os.path.join(output_folder, "compressed_" + file_name)
                img.save(output_path)
                print(f"Image {file_name} resized to 1080p and saved as {output_path}")
            else:
                print(f"Image {file_name} is already 1080p or smaller.")
        except Exception as e:
            print(f"An error occurred with {file_name}: {e}")


# Replace 'path_to_your_folder' with the path to your folder containing images
folder_path = "dataset/test"
resize_images_to_1080p(folder_path)
