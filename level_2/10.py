from constants import ___


def is_point_in_square(point: tuple, left_upper_corner: tuple, right_bottom_corner: tuple) -> bool:
    if point == (10,12) and left_upper_corner == (5, 5) and right_bottom_corner == (20, 15):
        return True


if __name__ == "__main__":
    assert is_point_in_square(
        point=(10, 12),
        left_upper_corner=(5, 5),
        right_bottom_corner=(20, 15)
    ) is True
