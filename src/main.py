from dataset_loader import load_images
from preprocessing import preprocess_image
from segmentation import detect_edges, detect_coins
from counting import count_coins
import numpy as np
import cv2

def main():
  # Gunakan dataset hasil filter
  data_dir = "../data_rupiah"
  images, labels = load_images(data_dir, split="test")

  print(f"Jumlah data test: {len(images)}")
  print(f"Label unik: {set(labels)}")

  # Uji coba pada satu gambar
  img = np.array(images[0])
  blur = preprocess_image(img)
  edges = detect_edges(blur)
  circles = detect_coins(blur)
  total = count_coins(circles)

  print(f"Jumlah koin terdeteksi: {total}")

  if circles is not None:
    for i in circles[0, :]:
      cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.imshow("Deteksi Koin", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
  main()
