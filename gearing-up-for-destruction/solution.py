def solution(pegs):
    
    even = len(pegs)%2==0
    num_dist = len(pegs)-1
    distances = [] 
    
    for i in range(num_dist):
        distances.append(pegs[i+1] - pegs[i])

    sum = 0
    sign = True
    for i in range(len(distances)):
        if sign:
            sum = sum + distances[i]
        else:
            sum = sum - distances[i]
        sign = not sign
    
    a = sum *2
    b = 3 if even else 1
    
    if a%b ==0 :
        a = a/b
        b = 1
    
    radius = a/b
    if radius<1: 
        return [-1,-1]
        
    for i in distances:
        if radius > (i-1) :
            return [-1,-1]
        radius = i - radius
        
    
    return [a,b]
    