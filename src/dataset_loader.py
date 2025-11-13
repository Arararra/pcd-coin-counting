import os
import json
from PIL import Image

def load_cat_to_name(data_dir):
  json_path = os.path.join(data_dir, "cat_to_name.json")
  with open(json_path) as f:
    return json.load(f)

def load_images(data_dir, split="train"):
  images = []
  labels = []
  cat_map = load_cat_to_name(data_dir)

  split_dir = os.path.join(data_dir, split)
  for class_id in sorted(os.listdir(split_dir)):
    class_path = os.path.join(split_dir, class_id)
    if not os.path.isdir(class_path):
      continue
    for img_name in os.listdir(class_path):
      if img_name.lower().endswith((".jpg", ".png", ".jpeg")):
        img_path = os.path.join(class_path, img_name)
        images.append(Image.open(img_path).convert("RGB"))
        labels.append(cat_map[class_id])
  return images, labels
