def operation_append(seq_list, seq_index, y):
    seq_list[seq_index].append(y)
    return None


def operation_find(seq_list, seq_index, y):
    seq = seq_list[seq_index]
    seq_size = len(seq)
    searched_element = seq[y % seq_size]
    return searched_element


operations = {
    1: operation_append,
    2: operation_find
}


def make_operation(operation, seq_list, seq_index, y):
    return operations.get(operation)(seq_list, seq_index, y)


def calculate_seq_index(x, last_answer, n):
    return (x ^ last_answer) % n


def dynamicArray(n, queries):
    seq_list = [[] for i in range(n)]
    last_answer = 0
    answers = []
    for query in queries:
        operation = query[0]
        result = make_operation(operation, seq_list, calculate_seq_index(query[1], last_answer, n), query[2])
        if result is not None:
            answers.append(result)
            last_answer = result

    return answers


if __name__ == '__main__':
    f = open("data.txt", "r")

    first_multiple_input = f.readline().strip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, f.readline().strip().split())))

    result = dynamicArray(n, queries)

    print(result)
