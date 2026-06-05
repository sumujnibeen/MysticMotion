import math

points = []


def add_point(x, y):

    points.append((x, y))

    if len(points) > 40:
        points.pop(0)


def clear_points():

    points.clear()


def get_points():

    return points


def get_motion_score():

    if len(points) < 2:
        return 0

    total = 0

    for i in range(1, len(points)):

        x1, y1 = points[i - 1]
        x2, y2 = points[i]

        total += math.hypot(
            x2 - x1,
            y2 - y1
        )

    return total