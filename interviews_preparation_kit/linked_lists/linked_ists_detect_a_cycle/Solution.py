def has_cycle(head):
    if head is None:
        return 0
    visited = [head.data]
    return has_cycle_next(head.next, visited)

def has_cycle_next(head, visited):
    if head is None:
        return 0
    if head.data in visited:
        return 1
    visited.append(head.data)
    return has_cycle_next(head.next, visited)
