numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"


def numbers_validator(text): return any([el in text for el in numbers])


def lower_case_validator(text): return any([el in text for el in lower_case])


def upper_case_validator(text): return any([el in text for el in upper_case])


def special_validator(text): return any([el in text for el in special_characters])


def minimumNumber(n, password):
    validators = [numbers_validator, lower_case_validator, upper_case_validator, special_validator]
    new_letters_to_add = len(
        list(filter(lambda result: result == False, [validator(password) for validator in validators])))
    letters_to_add = 0 if len(password) >= 6 else 6 - len(password)
    return max(letters_to_add, new_letters_to_add)


if __name__ == '__main__':
    f = open("data.txt", "r")

    n = int(f.readline().strip())

    password = f.readline().strip()

    result = minimumNumber(n, password)

    print(result)
