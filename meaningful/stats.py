def mean(l):
    n = len(l)
    return 1.0 / n * sum(x for x in l)

def variance(l):
    n = len(l)
    μ = mean(l)
    return 1.0 / n * sum(pow(x - μ, 2) for x in l)
