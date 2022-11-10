def mean(l):
    n = len(l)
    return 1.0 / n * sum(x for x in l)

def variance(l):
    mean_l = mean(l)
    n = len(l)
    return 1/(n) * sum((x-mean(l))**2 for x in l)  
