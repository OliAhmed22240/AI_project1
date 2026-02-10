import os
import csv

# Paths to dataset folders
images_dir = "data/images"     # Folder containing image files
labels_dir = "data/labels"     # Folder containing label files
csv_path = "data/CSVs/dataset.csv"  # Output CSV file path

# Get all image filenames
image_files = sorted(os.listdir(images_dir))

# Create and write the CSV file
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)

    # CSV header
    writer.writerow(["images", "labels"])

    # Create image–label pairs
    for img in image_files:
        image_path = os.path.join(images_dir, img)
        label_name = os.path.splitext(img)[0] + ".txt"
        label_path = os.path.join(labels_dir, label_name)
        writer.writerow([image_path, label_path])

print("dataset.csv created successfully")
