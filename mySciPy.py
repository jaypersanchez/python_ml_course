from scipy import integrate

# Define a simple function
def f(x):
    return x**2

# Compute the definite integral of f from 0 to 1
result, error = integrate.quad(f, 0, 1)
print("Integral result:", result)
