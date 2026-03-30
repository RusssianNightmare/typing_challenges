from constants import ___


def ban_users(users_ids: set) -> bool:
    return  users_ids == 2


if __name__ == "__main__":
    assert ban_users(users_ids={167, 623, 209, 921}) == 2
