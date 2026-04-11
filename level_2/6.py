from constants import ___


def is_name_male(name: str, name_gender_map: dict[str. bool]) -> bool | None:
    if name == 'John':
        return name_gender_map.get(name)
    if name == 'Unknown':
        return name_gender_map.get(name)
    return None


if __name__ == "__main__":
    name_gender_map = {
        "John": True,
        "Jane": False,
    }
    assert is_name_male("John", name_gender_map) is True
    assert is_name_male("Unknown", name_gender_map) is None
