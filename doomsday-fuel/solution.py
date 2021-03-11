from fractions import Fraction

def find_lcm(num1, num2):
    if(num1>num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while(rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2)/int(gcd))
    return lcm

def lcm(fractions):
    denoms = [f.denominator for f in fractions]
    
    num1 = denoms[0]
    num2 = denoms[1]
    lcm = find_lcm(num1, num2)
    
    for i in range(2, len(denoms)):
        lcm = find_lcm(lcm, denoms[i]) 
        
    return lcm

def transposeMatrix(m):
    return list(map(list,zip(*m)))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

    
def solution(m):
    
    if(len(m)==1):
        return [1,1]
        
    abs_states = []
    norm_states = []
    row_sum = []
    
    for i in range(len(m)):
        row = m[i]
        sum = 0 
        all_zeroes = True
        for col in row:
            sum = sum + col
            if col!=0:
                all_zeroes = False
        row_sum.append(sum)
        if(all_zeroes):
            abs_states.append(i)
        else:
            norm_states.append(i)
    
    Q = [[Fraction(0,1)]*len(norm_states)]*len(norm_states)
    R = [[Fraction(0,1)]*len(abs_states)]*len(norm_states)
        
    for i in range(len(norm_states)):
        state = norm_states[i]
        row = m[state]
        
        r_row = []
        for j in range(len(abs_states)):
            temp = abs_states[j]
            r_row.append(Fraction(row[temp],row_sum[state]))
        R[i] = r_row
        
        q_row = []
        for j in range(len(norm_states)):
            temp = norm_states[j]
            q_row.append(Fraction(row[temp],row_sum[state]))
        Q[i] = q_row
        
    I = []
            
    for i in range(len(Q)):
        row = []
        for j in range(len(Q)):
            row.append(Fraction(1 if i==j else 0))
        I.append(row)
            
    
    temp = []
    for i in range(len(Q)):
        row = []
        for j in range(len(Q)):
            row.append(I[i][j]-Q[i][j])
        temp.append(row)
    
    F = getMatrixInverse(temp)
    
    FR = []
    for i in range(len(R)):
        row = []
        for j in range(len(R[0])):
            row.append(Fraction(0,1))
        FR.append(row)
    
    for i in range(len(F)):
        for j in range(len(R[0])):
            for k in range(len(R)):
                FR[i][j] += F[i][k] * R[k][j]
    
    common = lcm(FR[norm_states[0]])

    answer = []
    for f in FR[0]:
        mul = common // f.denominator if f.numerator!=0 else 1
        answer.append(mul*f.numerator)
    
    answer.append(common)
    
    return answer

    