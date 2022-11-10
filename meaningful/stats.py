def mean(l):
    n = len(l)
    return 1.0 / n * sum(x for x in l)

def variance(l):
    n = len(l)
    mu = mean(l)
    print('Hello you!')
    return sum((x - mu)**2 for x in l) / n
