def solution(x, y):
    # Your code here
    
    if x == "1" and y == "1" :
        return "0"
    
    m = int(x)
    f = int(y)
    
    step = 0
    if m < 1 or f < 1 or m==f:
        return "impossible"
    
    if m>f:
        larger = m
        smaller = f
    else:
        larger = f
        smaller = m
    
    while larger>0 and smaller>0:
        if smaller==1:
            step = step + larger//smaller -1
            break
        else:
            whole = larger//smaller
            remainder = larger%smaller
            
            larger = smaller
            smaller = remainder
            
            step = step + whole
    
    if smaller < 1 or larger <1 :
        return "impossible"
        
    return str(step)
    