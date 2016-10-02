#Glia puzzles

def anonymous(x):
    return x**2 + 1


def integrate(fun, start, end):
    step = 0.1
    intercept = start
    area = 0

    while intercept < end:
        intercept += step
        if intercept > end+step/2: continue #Prevent the inprecise number at the end
        area += step*(fun(intercept-step)+fun(intercept))/2
    return area

print(integrate(anonymous, 0, 10))