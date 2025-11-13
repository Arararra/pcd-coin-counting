import cv2
import numpy as np

def detect_edges(img):
  edges = cv2.Canny(img, 100, 200)
  return edges

def detect_coins(img):
  circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 50,
                             param1=100, param2=30, minRadius=20, maxRadius=100)
  if circles is not None:
    circles = np.uint16(np.around(circles))
  return circles
