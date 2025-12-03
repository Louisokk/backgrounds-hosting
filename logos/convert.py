from PIL import Image
import os

def create_previews():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    preview_dir = os.path.join(current_dir, "previews")

    # Ordner erstellen, falls nicht vorhanden
    os.makedirs(preview_dir, exist_ok=True)

    # Alle GIFs im Ordner finden
    for filename in os.listdir(current_dir):
        if filename.lower().endswith(".gif"):
            gif_path = os.path.join(current_dir, filename)
            base_name = os.path.splitext(filename)[0]
            jpg_path = os.path.join(preview_dir, f"{base_name}.jpg")

            print(f"Processing {filename} ...")

            with Image.open(gif_path) as img:
                img.seek(0)  # Erstes Frame

                # Seitenverhältnis beibehalten → Zielbreite 150px
                w_percent = 150 / float(img.width)
                new_height = int(float(img.height) * w_percent)

                img = img.convert("RGB")  # GIF → JPG
                resized = img.resize((150, new_height), Image.LANCZOS)

                resized.save(jpg_path, "JPEG", quality=90)

    print("Done! Previews saved in /previews/")

if __name__ == "__main__":
    create_previews()
