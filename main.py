import cv2
import os

from effects.overlay import overlay_rgba

from gesture.hand_tracker import (
    get_hand_landmarks
)

from gesture.strange_pose import (
    is_strange_pose
)

from gesture.spider_pose import (
    is_spider_pose
)

from gesture.strange_circle import (
    add_point,
    get_points,
    clear_points,
    get_motion_score
)

portal_frames = []

for file in sorted(
    os.listdir(
        "assets/transparent/portal"
    )
):

    if not file.endswith(".png"):
        continue

    img = cv2.imread(
        os.path.join(
            "assets/transparent/portal",
            file
        ),
        cv2.IMREAD_UNCHANGED
    )

    if img is not None:
        portal_frames.append(img)

web_frames = []

for file in sorted(
    os.listdir(
        "assets/transparent/web"
    )
):

    if not file.endswith(".png"):
        continue

    img = cv2.imread(
        os.path.join(
            "assets/transparent/web",
            file
        ),
        cv2.IMREAD_UNCHANGED
    )

    if img is not None:
        web_frames.append(img)

print("Portal Frames:", len(portal_frames))
print("Web Frames:", len(web_frames))

cap = cv2.VideoCapture(0)

portal_active = False
portal_frame = 0

portal_x = 100
portal_y = 100

web_active = False
web_frame = 0

web_x = 0
web_y = 0

portal_cooldown = 0
web_cooldown = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    landmarks = get_hand_landmarks(frame)

    if portal_cooldown > 0:
        portal_cooldown -= 1

    if web_cooldown > 0:
        web_cooldown -= 1

    if landmarks is not None:

        index_tip = landmarks[8]

        x = int(
            index_tip.x * frame.shape[1]
        )

        y = int(
            index_tip.y * frame.shape[0]
        )

        if is_strange_pose(landmarks):

            cv2.putText(
                frame,
                "DOCTOR STRANGE",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 255),
                2
            )

            add_point(x, y)

            motion_score = get_motion_score()

            if (
                motion_score > 250
                and not portal_active
                and portal_cooldown == 0
            ):

                portal_active = True
                portal_frame = 0

                portal_x = max(
                    0,
                    x - 150
                )

                portal_y = max(
                    0,
                    y - 150
                )

                portal_cooldown = 120

                clear_points()

        else:

            clear_points()

        if (
            is_spider_pose(landmarks)
            and not web_active
            and web_cooldown == 0
        ):

            web_active = True
            web_frame = 0

            wrist = landmarks[0]

            wrist_x = int(
                wrist.x * frame.shape[1]
            )

            wrist_y = int(
                wrist.y * frame.shape[0]
            )

            web_x = wrist_x - 125
            web_y = wrist_y - 125

            web_cooldown = 40

    if portal_active:

        portal = portal_frames[
            portal_frame
        ]

        portal = cv2.resize(
            portal,
            (300, 300)
        )

        frame = overlay_rgba(
            frame,
            portal,
            portal_x,
            portal_y,
            opacity=0.80
        )

        portal_frame += 1

        if portal_frame >= len(portal_frames):

            portal_active = False
            portal_frame = 0

    if web_active:

        web = web_frames[
            web_frame
        ]

        web = cv2.resize(
            web,
            (250, 250)
        )

        frame = overlay_rgba(
            frame,
            web,
            web_x,
            web_y,
            opacity=0.90
        )

        web_frame += 1

        if web_frame >= len(web_frames):

            web_active = False
            web_frame = 0

    points = get_points()

    for i in range(
        1,
        len(points)
    ):

        thickness = max(
            1,
            int(i / 3)
        )

        cv2.line(
            frame,
            points[i - 1],
            points[i],
            (0, 140, 255),
            thickness
        )

    for point in points:

        cv2.circle(
            frame,
            point,
            3,
            (0, 180, 255),
            -1
        )

    cv2.imshow(
        "HeroGest",
        frame
    )

    key = cv2.waitKey(30) & 0xFF

    if key == ord("c"):
        clear_points()

    if key == 27:
        break

cap.release()

cv2.destroyAllWindows()