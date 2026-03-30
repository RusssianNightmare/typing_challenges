from constants import ___


def calculate_total_spent_for_users(users_ids: set, users_ids_to_users_map: dict) -> bool:
    for i in users_ids:
        if i in users_ids_to_users_map:
            return sum(users_ids_to_users_map.get(i)[2]) == 192


if __name__ == "__main__":
    assert calculate_total_spent_for_users(
        users_ids={3, 6, 12, 15},
        users_ids_to_users_map={
            3: ("Ilya", 32, [102, 15, 63, 12]),
        },
    ) == 192
