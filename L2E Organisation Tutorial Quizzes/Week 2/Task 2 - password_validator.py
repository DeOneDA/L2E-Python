def has_min_length(password):
    if len(password) < 8:
        return False
    else:
        return True


def has_uppercase(password):
    for ch in password:
        if ch.isupper():
            return True
        else:
            continue
    return False


def has_lowercase(password):
    for ch in password:
        if ch.islower():
            return True
        else:
            continue
    return False


def has_digit(password):
    for ch in password:
        if ch.isdigit():
            return True
        else:
            continue
    return False  


def has_special(password):
    for ch in password:
        if not ch.isalnum() and ch != " ":
            return True
    return False


def is_valid_password(password):
    if has_min_length(password) and has_uppercase(password) and has_lowercase(password) and has_digit(password) and has_special(password):
        return True
    else:
        return False


# bonus
def get_failed_requirements(password):
    result = []
    if not has_min_length(password):
        result.append("min_length")
    if not has_uppercase(password):
        result.append("uppercase")
    if not has_lowercase(password):
        result.append("lowercase")
    if not has_digit(password):
        result.append("digit")
    if not has_special(password):
        result.append("special")

    return result