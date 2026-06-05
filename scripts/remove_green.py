import cv2
import numpy as np
import os

input_dir = "assets/frames/portal"
output_dir = "assets/transparent/portal"

os.makedirs(output_dir, exist_ok=True)

threshold = 20

files = sorted(os.listdir(input_dir))

for file in files:

    if not file.lower().endswith(".png"):
        continue

    image_path = os.path.join(
        input_dir,
        file
    )

    img = cv2.imread(image_path)

    if img is None:
        continue

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    alpha = np.where(
        gray <= threshold,
        0,
        255
    ).astype(np.uint8)

    rgba = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2BGRA
    )

    rgba[:, :, 3] = alpha

    output_path = os.path.join(
        output_dir,
        file
    )

    cv2.imwrite(
        output_path,
        rgba
    )

print("Black removed")
print("Saved:", output_dir)