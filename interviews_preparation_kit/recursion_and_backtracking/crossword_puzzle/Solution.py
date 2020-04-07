def is_horizontal_start_position(crossword, row, column):
    if crossword[row][column] != '+' and  crossword[row][column] != 'X':
        if column != 0 and (crossword[row][column - 1] != '+' and crossword[row][column - 1] != 'X'):
            return False
        if column == len(crossword) - 1:
            return False
        if crossword[row][column + 1] != '-':
            return False
        return True
    return False


def is_vertical_start_position(crossword, row, column):
    if crossword[row][column] != '+' and crossword[row][column] != 'X':
        if row != 0 and (crossword[row - 1][column] != '+' and crossword[row - 1][column] != 'X'):
            return False
        if row == len(crossword) - 1:
            return False
        if crossword[row + 1][column] != '-':
            return False
        return True
    return False


def get_horizontal_position(crossword, row, column):
    letter = crossword[row][column]
    result = ''
    while (letter != '+' and letter != 'X') and column < len(crossword):
        result += letter
        column += 1
        if column < len(crossword):
            letter = crossword[row][column]
    return result


def get_vertical_position(crossword, row, column):
    letter = crossword[row][column]
    result = ''
    while (letter != '+' and letter != 'X') and row < len(crossword):
        result += letter
        row += 1
        if row < len(crossword):
            letter = crossword[row][column]

    return result


def find_matching_words(position, words):
    result = []
    for candidate in words:
        if len(candidate) == len(position):
            flag = True
            for pos in range(len(candidate)):
                if candidate[pos] != position[pos] and position[pos] != '-':
                    flag = False
                    break
            if flag:
                result.append(candidate)
    return result


def update_crossword_horizontally_with_word(crossword, new_word, row, column):
    updated_crossword = crossword[:]
    current_word_pos = 0
    for pos in range(column, column + len(new_word)):
        updated_crossword[row] = updated_crossword[row][:]
        updated_crossword[row][pos] = new_word[current_word_pos]
        current_word_pos += 1
    return updated_crossword


def get_next_position(row, column, limit):
    if (column == limit-1):
        return (row + 1, 0)
    return (row, column+1)


def update_crossword_vertically_with_word(crossword, new_word, row, column):
    updated_crossword = crossword[:]
    current_word_pos = 0
    for pos in range(row, row + len(new_word)):
        updated_crossword[pos] = updated_crossword[pos][:]
        updated_crossword[pos][column] = new_word[current_word_pos]
        current_word_pos += 1
    return updated_crossword

def find_next_position(crossword, words, start_row, start_column):
    # print(*crossword, sep='\n')
    # print()
    if len(words) == 0:
        return crossword
    for row in range(start_row, len(crossword)):
        for column in range(start_column, len(crossword)):
            if is_horizontal_start_position(crossword, row, column):
                position = get_horizontal_position(crossword, row, column)
                candidates = find_matching_words(position, words)
                for candidate in candidates:
                    new_words = words[:]
                    new_words.remove(candidate)
                    updated_crossword = update_crossword_horizontally_with_word(crossword, candidate, row, column)
                    new_row, new_column = get_next_position(row, column, len(crossword))
                    if len(new_words) == 0:
                        return updated_crossword
                    if new_row != len(crossword):
                        result = find_next_position(updated_crossword, new_words, new_row, new_column)
                        if result is not None:
                            return result
                    # print(*updated_crossword, sep='\n')

                # print("start position: %s %s" % (row, column))
                # print(position)
                # print(candidates)
            if is_vertical_start_position(crossword, row, column):
                position = get_vertical_position(crossword, row, column)
                candidates = find_matching_words(position, words)
                for candidate in candidates:
                    new_words = words[:]
                    new_words.remove(candidate)
                    updated_crossword = update_crossword_vertically_with_word(crossword, candidate, row, column)
                    new_row, new_column = get_next_position(row, column, len(crossword))
                    if len(new_words) == 0:
                        return updated_crossword
                    if new_row != len(crossword):
                        result = find_next_position(updated_crossword, new_words, new_row, new_column)
                        if result is not None:
                            return result

                # print("vertical start position: %s %s" % (row, column))
                # print(position)
                # print(candidates)

        start_column = 0
    return None

def convert_to_array(crossword):
    for pos in range(len(crossword)):
        crossword[pos] = list(crossword[pos])


def convert_to_string_array(crossword):
    for pos in range(len(crossword)):
        crossword[pos] = ''.join(crossword[pos])


def crosswordPuzzle(crossword, words):
    convert_to_array(crossword)
    words = words.split(';')
    result = find_next_position(crossword, words, 0, 0)
    convert_to_string_array(result)
    return result


if __name__ == '__main__':
    f = open("data.txt", "r")

    crossword = []

    for _ in range(10):
        crossword_item = f.readline().strip()
        crossword.append(crossword_item)

    words = f.readline().strip()

    result = crosswordPuzzle(crossword, words)

    print(*result, sep='\n')

    f.close()
