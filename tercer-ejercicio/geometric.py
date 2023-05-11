from math import pow

def geometric_probability(n,p):
    q = 1-p
    return pow(q,n-1)*p

def geometric_mean(p):
    return 1/p

def geometric_variance(p):
    q = 1-p
    return q/pow(p,2)

def geometric(n,p):
    variance = geometric_variance(p)
    return {
        "probability":geometric_probability(n,p),
        "mean":geometric_mean(p),
        "variance":variance,
        "standard_deviation":sqrt(variance),
    }

