"""
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
Example 2:
print(destCity([["C","A"],["B","C"],["D","B"]]))
"""





def destCity(paths):
    cities = set()
    for path in paths:
        cities.add(path[0])

    for path in paths:
        if path[1] not in cities:
            return path[1]

print(destCity([["B","C"],["D","B"],["C","A"]]))
