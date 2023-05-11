from math import pow, factorial, sqrt

def combination(n,x):
    return factorial(n)/(factorial(x)*factorial(n-x))

def binomial_probability(n,x,p):
    q = 1-p
    comb_result = combination(n,x)
    return comb_result*pow(p,x)*pow(q,n-x)

def binomial_mean(n,p):
    return n*p

def binomial_variance(n,p):
    q = 1-p
    return n*p*q

def binomial(n,x,p):
    variance = binomial_variance(n,p)
    return {
        "probability":binomial_probability(n,x,p),
        "mean":binomial_mean(n,p),
        "variance":variance,
        "standard_deviation":sqrt(variance)
    }
