import sys
input = sys.stdin.readline
max_weight = int(input())
n = int(input())
list_weights = []
for j in range(n):
    weight = int(input())
    list_weights.append(weight)
    
def lessThanFourCars(n, max_weight):
    current_weight = 0
    iterations = 0
    cars = 0
    while iterations < n and current_weight <= max_weight:
        current_weight += list_weights[iterations]
        if current_weight <= max_weight:
            cars += 1
        iterations += 1
    return cars

if n >= 4:
    current_weight = list_weights[0] + list_weights[1] + list_weights[2] + list_weights[3] 
    if current_weight <= max_weight:
        cars = 4 
        iterations = 4
        while iterations < n and current_weight <= max_weight:
            current_weight += list_weights[iterations]
            current_weight -= list_weights[iterations - 4]
            if current_weight <= max_weight:
                cars += 1 
            iterations += 1 
        print(cars)
    else:
        cars = lessThanFourCars(n, max_weight)
        print(cars)
else:
    cars = lessThanFourCars(n, max_weight)
    print(cars)
