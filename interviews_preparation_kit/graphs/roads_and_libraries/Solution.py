#!/bin/python3


# Complete the roadsAndLibraries function below.
def visit_neighbours(visited_cities, roads, city_index):
    if not visited_cities[city_index]:
        visited_neighbours = 1
        visited_cities[city_index] = True

        for destination in roads.get(city_index, []):
            visited_neighbours += visit_neighbours(visited_cities, roads, destination)


    else:
        visited_neighbours = 0
    return visited_neighbours


def prepare_roads(roads, n):
    cities = {}
    for road in roads:
        city_roads = cities.get(road[0] - 1, [])
        city_roads.append(road[1] - 1)
        cities[road[0] - 1] = city_roads
        city_roads = cities.get(road[1] - 1, [])
        city_roads.append(road[0] - 1)
        cities[road[1] - 1] = city_roads
    return cities


def roadsAndLibraries(n, c_lib, c_road, roads):
    if c_lib <= c_road:
        return n * c_lib

    result = 0
    visited_cities = [False] * n
    roads = prepare_roads(roads, n)
    for city_index in range(n):
        if not visited_cities[city_index]:
            visited_cities_count = visit_neighbours(visited_cities, roads, city_index)
            result += c_lib + (visited_cities_count - 1) * c_road

    return result


if __name__ == '__main__':
    f = open("data.txt", "r")

    q = int(f.readline().strip())

    for q_itr in range(q):
        nmC_libC_road = f.readline().strip().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, f.readline().strip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        print(str(result) + '\n')
