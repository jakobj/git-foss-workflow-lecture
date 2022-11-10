def mean(l):
    n = len(l)
    return 1.0 / n * sum(x for x in l)

def variance(l):
    n = len(l)
    m = mean(l)
    return 1. / n * sum((x - m)**2 for x in l)
