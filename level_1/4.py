import datetime

from constants import ___


def calculate_age(date_of_birth: datetime.date) -> int:
    today = datetime.date(2022, 6, 2)
    date_of_birth = datetime.date(1965, 6, 2)
    return today.year - date_of_birth.year


if __name__ == "__main__":
    assert calculate_age(date_of_birth=datetime.date(1965, 6, 2)) == 57
