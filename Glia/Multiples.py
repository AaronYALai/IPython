#Glia puzzles

def multiples_below(N, l = [3,5]):
    Ans = set()
    for factor in l:
        for i in range(int(N/factor)):
            Ans.add(factor*(i+1))  #Use set add can avoid repetitions
    if N in Ans:
        Ans.remove(N) #if accidentally add N, remove it from the set
    answer = sum(Ans)
    print('The sum of all the multiples of',l,'below %d is %d'%(N,answer))
    return answer

multiples_below(1000)