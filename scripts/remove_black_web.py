import cv2
import numpy as np
import os

INPUT_DIR = "assets/frames/web"

OUTPUT_DIR = "assets/transparent/web"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)

threshold = 25

for file in sorted(os.listdir(INPUT_DIR)):

    if not file.endswith(".png"):
        continue

    path = os.path.join(
        INPUT_DIR,
        file
    )

    img = cv2.imread(path)

    if img is None:
        continue

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    alpha = np.where(
        gray < threshold,
        0,
        255
    ).astype(np.uint8)

    rgba = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2BGRA
    )

    rgba[:, :, 3] = alpha

    cv2.imwrite(
        os.path.join(
            OUTPUT_DIR,
            file
        ),
        rgba
    )

print("Black removed")