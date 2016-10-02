#Glia puzzles

def Largest_prime(N):
    Candidates = []  #Find all a, b such that a*b = N
    #Search start from the sqrt of N and downward
    for p in reversed(range(1,int((N)**0.5)+1)):  
        if (N/p)==int(N/p):
            Candidates.append(int(p))     #Store factors as candidates
            Candidates.append(int(N/p))
            
    for cand in sorted(Candidates,reverse=True): #find the largest prime candidates
        if is_prime(cand):
            print('The largest prime factor of %d is %d'%(N,cand))
            return cand
            
prime_cache={}
def is_prime(N):
    if N in prime_cache:
        return prime_cache[N]
    
    for n in reversed(range(1,int((N)**0.5)+1)): #Search start from the sqrt of N and downward
        if (N/n)==int(N/n) and n!= 1:
            prime_cache[N] = False
    if N not in prime_cache:
        prime_cache[N] = True
        
    return prime_cache[N]

Largest_prime(13195)
Largest_prime(600851475143)