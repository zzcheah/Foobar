def solution(xs):
    leftOut = -1001
    posCount = 0
    negCount = 0
    neutralCount = 0
    posProduct = 1
    negProduct = 1
    finalProduct = 1
    
    if len(xs) == 1 :
        if xs[0] < 0:
            return str(xs[0])
    
    for num in xs:
        if num == -1:
            neutralCount = neutralCount +1
        
        if num <-1:
            negProduct = negProduct * num
            negCount = negCount + 1
            if num>leftOut:
                leftOut = num
        
        if num >=1:
            posCount = posCount + 1
            posProduct = posProduct * num
            
    posProduct = 0 if posCount==0 else posProduct
    
    if negCount ==0:
        if neutralCount>0 and neutralCount%2==0:
            negProduct = 1
        else:
            negProduct = 0
    elif negCount==1:
        if neutralCount!=0:
            negProduct = negProduct * -1
        else:
            negProduct = 0
    else:
        if negProduct<0:
            if neutralCount!=0:
                negProduct = negProduct * -1
            else:
                negProduct = negProduct // leftOut
    

    if posProduct==0 and negProduct ==0:
        finalProduct = 0
    else:
        if posProduct==0:
            finalProduct = negProduct
        else:
            if negProduct==0:
                finalProduct = posProduct
            else:
                finalProduct = posProduct * negProduct
                
    return str(int(finalProduct))