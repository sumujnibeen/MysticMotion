import cv2
import os

frames = []

folder = "assets/transparent/portal"

for file in sorted(os.listdir(folder)):

    if file.endswith(".png"):

        img = cv2.imread(
            os.path.join(folder, file),
            cv2.IMREAD_UNCHANGED
        )

        frames.append(img)

for frame in frames:

    cv2.imshow(
        "Portal",
        frame
    )

    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()