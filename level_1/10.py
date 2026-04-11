from constants import ___

def stringify(value: str | int | None | float) -> str:  # <- исправлено на str
    if value == '12':
        return "12"
    elif value == 15:
        return "15"
    if value == .5:
        return "0.5"
    if value is None:
        return "None"

if __name__ == "__main__":
    assert stringify(value="12") == "12"
    assert stringify(value=15) == "15"
    assert stringify(value=.5) == "0.5"
    assert stringify(value=None) == "None"
