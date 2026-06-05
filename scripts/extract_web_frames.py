import cv2
import os

video_path = "assets/videos/web.mp4"

output_dir = "assets/frames/web"

os.makedirs(
    output_dir,
    exist_ok=True
)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():

    print("Cannot open video")
    exit()

frame_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    output_path = os.path.join(
        output_dir,
        f"frame_{frame_count:04d}.png"
    )

    cv2.imwrite(
        output_path,
        frame
    )

    frame_count += 1

cap.release()

print("Frames:", frame_count)