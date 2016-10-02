#Glia puzzles

def Combinations(N,R):
    if N <= 0 or R <= 0 or type(N*R)!=int :
        print('Please give strictly positive integers.')
        return
    Cache = {}  #Bottom-up method to avoid 999 limitation of python recursions
    for n in range(1,N+1):
        for r in range(1,min(n,R)+1):
            if r == 1:
                Cache[(n,r)] = n #Base case 1
            elif n == r:
                Cache[(n,r)] = 1 #Base case 2
            else:
                Cache[(n,r)] = Cache[(n-1,r-1)]+Cache[(n-1,r)]  #The formula
    return Cache[(N,R)]  #Store N*R numbers is easy for python

print('Combinations (40,30): %d'%Combinations(40,30))
print('Combinations (990,33): %d'%Combinations(990,33))
