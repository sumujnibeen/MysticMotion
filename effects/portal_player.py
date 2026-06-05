import cv2
import os

portal_frames = []

folder = "assets/transparent/portal"

for file in sorted(os.listdir(folder)):

    if not file.endswith(".png"):
        continue

    img = cv2.imread(
        os.path.join(folder, file),
        cv2.IMREAD_UNCHANGED
    )

    portal_frames.append(img)

print("Frames Loaded:", len(portal_frames))