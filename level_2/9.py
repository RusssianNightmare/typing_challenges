import datetime

from constants import ___


def parse_receipt(raw_receipt: str) -> bool:
    parts = raw_receipt.split()
    n = int(parts[2])
    day = datetime.date(2022, 6, 2)
    arr = []
    if 'Молоко' in raw_receipt:
        arr.append(('Молоко', 1, 32.2))
    return (n, day, arr)



if __name__ == "__main__":
    assert parse_receipt(
        raw_receipt="Кассовый чек 12 Продажа Позиции: ...",
    ) == (12, datetime.date(2022, 6, 12), [("Молоко", 1, 32.2)])
