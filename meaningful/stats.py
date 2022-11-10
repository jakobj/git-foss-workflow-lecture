def mean(l):
    n = len(l)
    return 1.0 / n * sum(x for x in l)

def variance(l):
    n = len(l)
    return 1.0/(n) * sum((l-mean(l))**2) 
