import numpy as np
from matplotlib import pyplot as plt
import objective_functions
import random

# Initializing all constants that the pso algorithm needs
THETA_MIN = 0.4
THETA_MAX = 0.9
NUMBER_OF_PARTICLES = 50
MAX_ITERATIONS = 500
DIMENSIONS = 2
C1 = C2 = 2
FUNCTION = "easom"

"""
This function initializes all the necessary data for the pso algorithm and returns them
d: a numpy array that contains all the boundaries for every variable
-> Notes:
The position of each particle is randomly chosen, always with respect to the boundaries
The current local minimum is equal to initial position
For the global minimum the best position is chosen based on the value of the objective function
All velocities are zero
"""
def initialize_swarm(d):
    particles = np.empty((NUMBER_OF_PARTICLES, DIMENSIONS + 1))
    local = np.empty((NUMBER_OF_PARTICLES, DIMENSIONS + 1))
    global_ = np.empty(DIMENSIONS + 1)
    v = np.zeros((NUMBER_OF_PARTICLES, DIMENSIONS))
    for i in range(0, NUMBER_OF_PARTICLES):
        for j in range(0, DIMENSIONS):
            particles[i][j] = d[j][0] + random.uniform(0, 1) * (d[j][1] - d[j][0])
            local[i][j] = particles[i][j]
        value_of_objective_function = objective_functions.objective_function(FUNCTION, particles[i])
        particles[i][DIMENSIONS] = local[i][DIMENSIONS] = value_of_objective_function
    best_index = np.argmin(particles[:, [DIMENSIONS]])
    global_[DIMENSIONS] = particles[best_index][DIMENSIONS]
    for i in range(0, DIMENSIONS):
        global_[i] = particles[best_index][i]
    return particles, local, global_, v

"""
This function updates the theta
i: is the number of iterations
"""
def update_theta(i):
    return THETA_MAX - ((THETA_MAX - THETA_MIN) / MAX_ITERATIONS) * i

"""
This function checks if the value of a variable is out of bounds and if so then it replaces it with the bound
value: an integer which is the value of the variable 
boundaries: numpy array that stores the constraints of the variable
"""
def in_bound_value(value, boundaries):
    new_value = value
    if value < boundaries[0]:
        new_value = boundaries[0]
    elif value > boundaries[1]:
        new_value = boundaries[1]
    return new_value

"""
This function updates the velocities, the positions, the local best of each particle and the global best 
p: numpy array where all positions of the particles and the value of the objective function are stored
l: numpy array where the best position for each particle and the value of the objective function are stored
g: numpy array where the best position among all particles and the value of the objective function are stored
v: numpy array where the velocities of all particles are stored
d: numpy array that contains the boundaries of all variables
th: inertia theta
"""
def update_position_local_and_global_minimums(p, l, g, v, d, th):
    # For each particle
    for i in range(0, NUMBER_OF_PARTICLES):
        # Update its velocity
        for j in range(0, DIMENSIONS):
            v[i][j] = th * v[i][j] + C1 * random.uniform(0, 1) * (l[i][j] - p[i][j]) + C2 * random.uniform(0, 1) * (g[j] - p[i][j])
        # Update its position
        for j in range(0, DIMENSIONS):
            p[i][j] = in_bound_value(particles_position[i][j] + v[i][j], d[j])
        p[i][DIMENSIONS] = objective_functions.objective_function(FUNCTION, p[i])
        # Update local minimum
        if l[i][DIMENSIONS] > p[i][DIMENSIONS]:
            for j in range(0, DIMENSIONS + 1):
                l[i][j] = p[i][j]
        # Update global minimum
        if l[i][DIMENSIONS] < g[DIMENSIONS]:
            for j in range(0, DIMENSIONS + 1):
                g[j] = p[i][j]
    return p, v, l, g


"""
This function is used for plotting the graph
img: A list of 2 lists where in the first list the points of the y axis are stored and in the second the points of the x-axis are stored
"""
def plot(img):
    y = np.array(img[0])
    x = np.array(img[1])
    plt.plot(x, y)
    plt.xlabel("Iteration Number")
    plt.ylabel("Global best")
    # plt.savefig(f"plot_{FUNCTION}")
    plt.show()

# !---------------------> MAIN PROGRAM <---------------------!

# Initializing data
domain = objective_functions.get_constraints(FUNCTION)
image = [[], []]

# Initializing the positions of every particle that belongs to the swarm
particles_position, local_best, global_best, velocity = initialize_swarm(domain)

# Loop
for iteration in range(0, MAX_ITERATIONS):

    # Updating theta
    theta = update_theta(iteration)

    # Update particles position, velocity, local best and global best
    particles_position, velocity, local_best, global_best = update_position_local_and_global_minimums(particles_position, local_best, global_best, velocity, domain, theta)

    # Updating image for the plot
    image[0].append(global_best[DIMENSIONS])
    image[1].append(iteration)


print(f"Global Best is: f({global_best[0]},{global_best[1]}) = {global_best[2]}")

plot(image)

