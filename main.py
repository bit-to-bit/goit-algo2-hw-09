import random
import math

def sphere_function(x):
    return sum(xi ** 2 for xi in x)

def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    n = len(bounds)
    current_x = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_x)
    step_size = 0.1

    for _ in range(iterations):
        neighbor_x = [
            min(max(current_x[i] + random.uniform(-step_size, step_size), bounds[i][0]), bounds[i][1])
            for i in range(n)
        ]
        neighbor_value = func(neighbor_x)
        
        if neighbor_value < current_value:
            value_diff = abs(current_value - neighbor_value)
            pos_diff = sum((neighbor_x[i] - current_x[i])**2 for i in range(n))**0.5
            
            current_x, current_value = neighbor_x, neighbor_value
            
            if value_diff < epsilon or pos_diff < epsilon:
                break

    return current_x, current_value

def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    n = len(bounds)
    current_x = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_x)
    
    for _ in range(iterations):
        neighbor_x = [random.uniform(b[0], b[1]) for b in bounds]
        neighbor_value = func(neighbor_x)
        
        if neighbor_value < current_value:
            value_diff = abs(current_value - neighbor_value)
            pos_diff = sum((neighbor_x[i] - current_x[i])**2 for i in range(n))**0.5
            
            current_x, current_value = neighbor_x, neighbor_value
            
            if value_diff < epsilon or pos_diff < epsilon:
                break
                
    return current_x, current_value

def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    n = len(bounds)
    current_x = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_x)
    
    for _ in range(iterations):
        if temp < epsilon:
            break
            
        neighbor_x = [
            min(max(current_x[i] + random.uniform(-0.5, 0.5), bounds[i][0]), bounds[i][1])
            for i in range(n)
        ]
        neighbor_value = func(neighbor_x)
        
        delta = neighbor_value - current_value
        
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_x, current_value = neighbor_x, neighbor_value
            
        temp *= cooling_rate
        
    return current_x, current_value

if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
