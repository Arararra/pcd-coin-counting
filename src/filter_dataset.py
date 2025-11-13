import os
import json
import shutil

def filter_rupiah_dataset(data_dir="data", output_dir="data_rupiah"):
  # Muat kategori dari JSON
  with open(os.path.join(data_dir, "cat_to_name.json")) as f:
    cat_map = json.load(f)

  # ID koin rupiah
  rupiah_ids = ["81", "82", "83", "84", "85"]

  # Buat folder output
  for split in ["train", "validation", "test"]:
    src_split = os.path.join(data_dir, split)
    dst_split = os.path.join(output_dir, split)
    os.makedirs(dst_split, exist_ok=True)

    for rupiah_id in rupiah_ids:
      src_class = os.path.join(src_split, rupiah_id)
      dst_class = os.path.join(dst_split, rupiah_id)
      if os.path.exists(src_class):
        shutil.copytree(src_class, dst_class, dirs_exist_ok=True)

  # Simpan cat_to_name.json versi rupiah saja
  filtered_map = {k: v for k, v in cat_map.items() if k in rupiah_ids}
  os.makedirs(output_dir, exist_ok=True)
  with open(os.path.join(output_dir, "cat_to_name.json"), "w") as f:
    json.dump(filtered_map, f, indent=4)

  print("✅ Dataset khusus koin Rupiah berhasil dibuat di:", output_dir)


if __name__ == "__main__":
  filter_rupiah_dataset()
