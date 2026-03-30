from constants import sre_constants


def is_user_banned(user_id: int) -> bool:
    return user_id == 32


if __name__ == "__main__":
    assert is_user_banned(user_id=32) is True
