from constants import ___


def calculate_total_spent_for_user(user: tuple) -> bool:
    sum_c = sum(user[2])
    return sum_c == 192


if __name__ == "__main__":
    assert calculate_total_spent_for_user(user=("Ilya", 32, [102, 15, 63, 12])) == 192
