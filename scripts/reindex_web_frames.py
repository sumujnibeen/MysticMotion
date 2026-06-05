import os
import shutil

INPUT_DIR = "assets/transparent/web"
OUTPUT_DIR = "assets/transparent/web_final"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)

start_frame = 19
end_frame = 112

new_index = 0

for old_index in range(
    start_frame,
    end_frame + 1
):

    old_name = (
        f"frame_{old_index:04d}.png"
    )

    old_path = os.path.join(
        INPUT_DIR,
        old_name
    )

    if not os.path.exists(old_path):
        continue

    new_name = (
        f"frame_{new_index:04d}.png"
    )

    new_path = os.path.join(
        OUTPUT_DIR,
        new_name
    )

    shutil.copy2(
        old_path,
        new_path
    )

    new_index += 1

print(
    f"Created {new_index} frames"
)