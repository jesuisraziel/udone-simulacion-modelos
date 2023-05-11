from math import pow, factorial, exp

def poisson_probability(x, beta):
    denominator = factorial(x)
    return (pow(beta,x)*exp(-(beta)))/denominator

def poisson_mean(beta):
    return beta

def poisson_variance(beta):
    return beta

def poisson(x,beta):
    variance = poisson_variance(beta)
    return {
        "probability":poisson_probability(x,beta),
        "mean":poisson_mean(beta),
        "variance":variance,
        "standard_deviation":sqrt(variance)
    }

