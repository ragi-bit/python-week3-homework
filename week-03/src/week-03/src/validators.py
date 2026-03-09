def is_email(text):
    return "@" in text and "." in text


def is_phone_number(text):
    if text.startswith("+371 ") and len(text) == 13:
        return text[5:].isdigit()
    return False


def is_valid_age(age):
    return isinstance(age, int) and 0 <= age <= 150


def is_strong_password(text):
    if len(text) < 8:
        return False

    has_digit = False
    has_letter = False

    for c in text:
        if c.isdigit():
            has_digit = True
        if c.isalpha():
            has_letter = True

    return has_digit and has_letter


def is_valid_date(text):
    parts = text.split("-")

    if len(parts) != 3:
        return False

    year, month, day = parts

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    month = int(month)
    day = int(day)

    return 1 <= month <= 12 and 1 <= day <= 31


if __name__ == "__main__":
    print(is_email("test@test.lv"))
    print(is_email("test"))