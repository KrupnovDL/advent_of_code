# The next year, just to show off, Santa decides to take the route with the longest distance instead.
#
# He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.
#
# For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.
#
# What is the distance of the longest route?


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
longest_distance_overall = float("-inf")

for starting_citi in cities:
    cities_to_visit = list(cities)
    current_citi = starting_citi
    cities_to_visit.remove(current_citi)
    distance = 0
    for i in range(len(cities_to_visit)):
        longest_distance = float("-inf")
        next_citi = None
        for citi in cities_to_visit:
            if graph[current_citi][citi] > longest_distance:
                longest_distance = graph[current_citi][citi]
                next_citi = citi
        distance += graph[current_citi][next_citi]
        current_citi = next_citi
        cities_to_visit.remove(current_citi)
    if distance > longest_distance_overall:
        longest_distance_overall = distance

print(longest_distance_overall)
