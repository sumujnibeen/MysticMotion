import numpy as np


def overlay_rgba(
    background,
    overlay,
    x,
    y,
    opacity=0.80
):

    bg_h, bg_w = background.shape[:2]
    ov_h, ov_w = overlay.shape[:2]

    if x >= bg_w or y >= bg_h:
        return background

    if x + ov_w <= 0 or y + ov_h <= 0:
        return background

    x1 = max(0, x)
    y1 = max(0, y)

    x2 = min(bg_w, x + ov_w)
    y2 = min(bg_h, y + ov_h)

    overlay_x1 = x1 - x
    overlay_y1 = y1 - y

    overlay_x2 = overlay_x1 + (x2 - x1)
    overlay_y2 = overlay_y1 + (y2 - y1)

    roi = background[y1:y2, x1:x2]

    overlay_crop = overlay[
        overlay_y1:overlay_y2,
        overlay_x1:overlay_x2
    ]

    alpha = (
        overlay_crop[:, :, 3] / 255.0
    ) * opacity

    alpha = alpha[:, :, np.newaxis]

    roi[:] = (
        alpha * overlay_crop[:, :, :3]
        + (1 - alpha) * roi
    ).astype(np.uint8)

    return background