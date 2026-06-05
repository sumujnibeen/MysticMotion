import os

folder = "assets/transparent/portal"

files = sorted(
    f for f in os.listdir(folder)
    if f.endswith(".png")
)

kept = []

for file in files:

    n = int(
        file.replace("frame_", "")
            .replace(".png", "")
    )

    if 1 <= n <= 180:
        kept.append(file)
    else:
        os.remove(
            os.path.join(folder, file)
        )

for i, file in enumerate(kept):

    old_path = os.path.join(
        folder,
        file
    )

    temp_path = os.path.join(
        folder,
        f"temp_{i:04d}.png"
    )

    os.rename(
        old_path,
        temp_path
    )

temp_files = sorted(
    f for f in os.listdir(folder)
    if f.startswith("temp_")
)

for i, file in enumerate(temp_files):

    old_path = os.path.join(
        folder,
        file
    )

    new_path = os.path.join(
        folder,
        f"frame_{i:04d}.png"
    )

    os.rename(
        old_path,
        new_path
    )

print("Done")