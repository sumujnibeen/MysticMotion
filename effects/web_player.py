import cv2
import os

web_frames = []

folder = "assets/transparent/web"

for file in sorted(os.listdir(folder)):

    if not file.lower().endswith(".png"):
        continue

    img = cv2.imread(
        os.path.join(folder, file),
        cv2.IMREAD_UNCHANGED
    )

    if img is not None:
        web_frames.append(img)

print("Web Frames:", len(web_frames))