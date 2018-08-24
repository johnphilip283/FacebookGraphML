import random

with open('huge_network.txt', 'r') as source:
    data = [(random.random(), line) for line in source]

data.sort()

with open('shuffled_network.txt', 'w') as target:
    for _, line in data:
        target.write(line)
