import cv2
import os

video_path = "assets/videos/portal.mp4"
output_dir = "assets/frames/portal"

os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    raise FileNotFoundError(video_path)

frame_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imwrite(
        os.path.join(
            output_dir,
            f"frame_{frame_count:04d}.png"
        ),
        frame
    )

    frame_count += 1

cap.release()

print("Frames:", frame_count)