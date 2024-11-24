import json

# Name der Input- und Output-Dateien
input_file = "backgrounds.json"
output_file = "backgrounds_with_preview.json"

def add_preview_to_items():
    # JSON-Datei laden
    with open(input_file, "r") as file:
        data = json.load(file)

    # Über alle Items iterieren und "preview" hinzufügen
    for item in data["items"]:
        if "image" in item:
            item["preview"] = "preview/" + item["image"]

    # Neue JSON-Datei speichern
    with open(output_file, "w") as file:
        json.dump(data, file, indent=2)

    print(f"Updated JSON with 'preview' keys saved to {output_file}.")

if __name__ == "__main__":
    add_preview_to_items()
