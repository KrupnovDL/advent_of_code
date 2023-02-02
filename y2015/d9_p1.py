# --- Day 9: All in a Single Night ---
# Every year, Santa manages to deliver all of his presents in a single night.
#
# This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?
#
# For example, given the following distances:
#
# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
# The possible routes are therefore:
#
# Dublin -> London -> Belfast = 982
# London -> Dublin -> Belfast = 605
# London -> Belfast -> Dublin = 659
# Dublin -> Belfast -> London = 659
# Belfast -> Dublin -> London = 605
# Belfast -> London -> Dublin = 982
# The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.
#
# What is the distance of the shortest route?


from input_data import input_data


input_data = input_data(2015, 9).splitlines()
graph = {}

for string in input_data:
    string = string.split()
    graph.setdefault(string[0], {})
    graph.setdefault(string[2], {})
    graph[string[2]][string[0]] = graph[string[0]][string[2]] = int(string[-1])
# graph["London"] = {}
# graph["Dublin"] = {}
# graph["Belfast"] = {}
# graph["London"]["Dublin"] = 464
# graph["London"]["Belfast"] = 518
# graph["Belfast"]["Dublin"] = 141
# graph["Belfast"]["London"] = 518
# graph["Dublin"]["London"] = 464
# graph["Dublin"]["Belfast"] = 141


cities = tuple(graph.keys())
shortest_distance_overall = float("inf")

for starting_city in cities:
    cities_to_visit = list(cities)
    current_city = starting_city
    cities_to_visit.remove(current_city)
    distance = 0
    for i in range(len(cities_to_visit)):
        shortest_distance = float("inf")
        next_city = None
        for city in cities_to_visit:
            if graph[current_city][city] < shortest_distance:
                shortest_distance = graph[current_city][city]
                next_city = city
        distance += graph[current_city][next_city]
        current_city = next_city
        cities_to_visit.remove(current_city)
    if distance < shortest_distance_overall:
        shortest_distance_overall = distance

print(shortest_distance_overall)
