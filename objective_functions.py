import math
import numpy as np

def get_constraints(function_name):
    if function_name == "matyas":
        boundaries = np.array([[-10, 10], [-10, 10]])
    elif function_name == "easom":
        boundaries = np.array([[-100, 100], [-100, 100]])
    elif function_name == "sphere":
        boundaries = np.array([[-100, 100], [-100, 100]])
    elif function_name == "ackley":
        boundaries = np.array([[-5, 5], [-5, 5]])
    elif function_name == "bukin":
        boundaries = np.array([[-15, -5], [-3, 3]])
    elif function_name == "himmelblau":
        boundaries = np.array([[-5, 5], [-5, 5]])
    elif function_name == "three-hump":
        boundaries = np.array([[-5, 5], [-5, 5]])
    elif function_name == "eggholder":
        boundaries = np.array([[-512, 512], [-512, 512]])
    elif function_name == "cross-in-tray":
        boundaries = np.array([[-10, 10], [-10, 10]])
    else:
        boundaries = None
    return boundaries

def objective_function(function_name, variables):
    x = variables[0]
    y = variables[1]
    if function_name == "matyas":
        value = 0.26 * (x**2 + y**2) - 0.48*x*y
    elif function_name == "easom":
        value = -(math.cos(x) * math.cos(y) * math.exp(-((x - math.pi)**2 + (y - math.pi)**2)))
    elif function_name == "sphere":
        value = x**2 + y**2
    elif function_name == "ackley":
        value = -20*math.exp(-0.2*math.sqrt(0.5*(x**2+y**2))) - math.exp(0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) + math.e + 20
    elif function_name == "bukin":
        value = 100*math.sqrt(abs(y - 0.01*(x**2))) + 0.01*abs(x + 10)
    elif function_name == "himmelblau":
        value = (x**2 + y - 11)**2 + (x + y**2 - 7)**2
    elif function_name == "three-hump":
        value = 2*(x**2) - 1.05*(x**4) + (x**6)/6 + x*y + y**2
    elif function_name == "eggholder":
        value = - (y + 47)*math.sin(math.sqrt(abs(x/2 + (y+47)))) - x*math.sin(math.sqrt(abs(x - (y + 47))))
    elif function_name == "cross-in-tray":
        value = -0.0001 * (abs(math.sin(x) * math.sin(y)) * math.exp(abs(100 - (math.sqrt(x**2 + y**2) / math.pi))) + 1) ** 0.1
    else:
        value = None
    return value