

def superReducedString(str):
    position = 0
    while position+1 < len(str):
        if str[position] == str[position+1]:
            str = str[0:position] + str[position+2:]
            if position > 0:
                position -= 1
        else:
            position += 1
    return 'Empty String' if str == '' else str


if __name__ == '__main__':
    f = open("data.txt", "r")

    str = f.readline().strip()

    result = superReducedString(str)

    print(result)

