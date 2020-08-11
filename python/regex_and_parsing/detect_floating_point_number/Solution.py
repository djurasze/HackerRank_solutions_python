import re

p = re.compile('^([+-])?([0-9])*([.])[0-9]+$')

def is_floating(test_case):
    return True if p.match(test_case) else False


if __name__ == '__main__':
    f = open("data.txt", "r")

    num_of_tests_cases = int(f.readline().strip())

    tests = [f.readline().strip() for _ in range(0,num_of_tests_cases)]

    for test_case in tests:
        print(is_floating(test_case))


