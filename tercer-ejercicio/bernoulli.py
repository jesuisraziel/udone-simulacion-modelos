from binomial import binomial_probability, binomial_mean, binomial_variance

def bernoulli_probability(x,p):
    if (x != 1) and (x != 0):
        raise Exception("Invalid parameter for number of successes");
    if (p > 1) or (p < 0):
        raise Exception("Invalid parameter for probability of success");
    return binomial_probability(1, x, p)

def bernoulli_mean(p):
    return binomial_mean(1,p)

def bernoulli_variance(p):
    return binomial_variance(1,p)

def bernoulli(n,x,p):
    variance = bernoulli_variance(n,p)
    return {
        "probability":bernoulli_probability(x,p),
        "mean":bernoulli_mean(n,p),
        "variance":variance,
        "standard_deviation":sqrt(variance)
    }
