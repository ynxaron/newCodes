coordinates = [(a, a + 1) for a in range(1, 10)]
print(coordinates)

results = [a * b for (a, b) in coordinates]
print(results)

evaluations = ["Bigger" if res > 15 else "Smaller" for res in results]
print(evaluations)
