#!/bin/python3


def find_princess(grid):
    last_index = len(grid) - 1
    if grid[0][0] == 'p':
        return (0,0)
    if grid[0][last_index] == 'p':
        return (0, last_index)
    if grid[last_index][0] == 'p':
        return (last_index, 0)
    else:
        return (last_index, last_index)


def displayPathtoPrincess(m, grid):
    princess_position = find_princess(grid)
    number_of_steps_in_one_direction = (len(grid) - 1)//2
    steps = ["UP"]*number_of_steps_in_one_direction if princess_position[0] == 0 else ["DOWN"]*number_of_steps_in_one_direction
    steps += ["LEFT"]*number_of_steps_in_one_direction if princess_position[1] == 0 else ["RIGHT"]*number_of_steps_in_one_direction

    print(*steps, sep='\n')


if __name__ == '__main__':
    f = open("data.txt", "r")

    m = int(f.readline().strip())
    grid = []
    for i in range(0, m):
        grid.append(f.readline().strip().strip())

    displayPathtoPrincess(m, grid)
