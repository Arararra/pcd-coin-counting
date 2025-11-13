import cv2
import numpy as np

def load_image(path):
  img = cv2.imread(path)
  if img is None:
    raise FileNotFoundError(f"Gambar tidak ditemukan: {path}")
  return img

def preprocess_image(img):
  if isinstance(img, np.ndarray):
    src = img
  else:
    src = np.array(img)
  gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
  blur = cv2.GaussianBlur(gray, (5, 5), 0)
  return blur
