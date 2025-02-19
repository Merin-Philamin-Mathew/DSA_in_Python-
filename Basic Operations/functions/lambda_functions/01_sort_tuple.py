# example 1
data = [(1, 2), (3, 1), (5, 4)]
data.sort(key=lambda x: x[0])
print(data)  # Output: [(3, 1), (1, 2), (5, 4)]

# example 2
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True ,key=lambda x: len(x))
print(cars)

# example 3