def is_open_palm(landmarks):

    index_up = landmarks[8].y < landmarks[6].y
    middle_up = landmarks[12].y < landmarks[10].y
    ring_up = landmarks[16].y < landmarks[14].y
    pinky_up = landmarks[20].y < landmarks[18].y

    return (
        index_up and
        middle_up and
        ring_up and
        pinky_up
    )