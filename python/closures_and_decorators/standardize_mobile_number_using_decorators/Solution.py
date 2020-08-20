def normalize_number(raw):
    return "+91 " + raw[-10:-5] + " " + raw[-5:]


def normalize_numbers(operation):
    def wrapper(raw_numbers):
    
        return operation(map(lambda raw: normalize_number(raw), raw_numbers))

    return wrapper


@normalize_numbers
def sort_phones(numbers):
    return sorted(numbers)


if __name__ == '__main__':
    f = open("data.txt", "r")

    first_multiple_input = f.readline().strip().split()

    n = int(first_multiple_input[0])

    raw_numbers = [f.readline().strip() for el in range(n)]

    print(*sort_phones(raw_numbers), sep="\n")
